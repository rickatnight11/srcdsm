#!/usr/bin/python
""" srcds Server Manager
by Rick White (rickatnight11@gmail.com)
"""
"""
Imports
"""
import ConfigParser
import os, os.path
import sys
from optparse import OptionParser

"""
Global Variables
"""
#Verbosity can be 0 (silent), 1 (default), or 2 (noisy)
_verbosity = 1

#Location of srcdsm config file (default is /etc/srcdsm/srcdsm.conf)
_config_file='/etc/srcdsm/srcdsm.conf'
_config_file = os.path.normpath(_config_file)

#Location of deployments config file (populated by config file)
_deployments_conf= ''

#Directory to deploy srcds installations, if not specified (populated by config file)
_default_install_dir = ''

#Directory containing gametype configs (populated by config file)
_gametypes_dir = ''

#List of known game types
game_types=[]

#List of installed deployments
deployments=[]

#List of installed instances 
instances=[]

"""
Logic
"""

def ProcessArgs():
    global _verbosity
    
    #Define option/argument parser
    parser = OptionParser(usage='usage: %prog [OPTIONS]', version='%prog 0.1')
    parser.add_option('-d', '--deploy', action='store_true', dest='deploy', help='deploy new installation of SRCDS', default=False)
    parser.add_option('-i', '--install', action='store_true', dest='install', help='install new instance of a game', default=False)
    parser.add_option('-s', '--start', action='store_true', dest='start', help='start a game', default=False)
    parser.add_option('-e', '--stop', action='store_true', dest='stop', help='stop a game', default=False)
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='increase verbosity (enable debug mode)', default=False)
    parser.add_option('-q', '--quiet', action='store_true', dest='quiet', help='decrease verbosity (enable silent mode)', default=False)
    
        
    (options, args) = parser.parse_args()
    
    #Check for extra arguments
    if len(args) > 0:
        parser.error("too many arguments passed")
    
    #Check for verbosity switches
    if options.verbose and options.quiet:
        PrintMessage('Both --verbose and --quiet switches used.  Defaulting to normal verbosity', 2)
    elif options.verbose:
        _verbosity = 2
    elif options.quiet:
        _verbosity = 0
    
    #Check for mutually exclusive 'action' switches
    actionlist = []
    if options.deploy:
        actionlist.append('--deploy')
    if options.install:
        actionlist.append('--install')
    if options.start:
        actionlist.append('--start')
    if options.stop:
        actionlist.append('--stop')
    
    #List superfluous action switches used
    if len(actionlist) > 1:
        error_message = 'Cannot use more than one action switch at a time ('
        index = 0
        for action in actionlist:
            if index > 0:
                error_message += ', '
            error_message += action
            index += 1
        error_message += ')'
        parser.error(error_message)
    
    


def ReadConf():
    #Check existence and permissions of config file
    if os.path.isfile(_config_file) and os.R_OK(_config_file):
        
        #Parse config file
        try:
            config = ConfigParser.SafeConfigParser()
            config.read(_config_file)
        except IOError:
            PrintMessage('cannot open' + _config_file, 0)
            return False
        else:
            PrintMessage('Loaded Config File (' + _config_file + ')', 3)
    elif not os.path.isfile(_config_file):
        PrintMessage(_config_file + ' does not exist!', 0)
        return False
    elif not os.R_OK(_config_file):
        PrintMessage('Insufficient permissions to read ' + _config_file + '!', 0)
        return False
    else:
        PrintMessage('Unknown error attempting to load config file!', 0)
        return False
    
    #Load default variables
    defaults = dict(config.items('settings'))
    if defaults.has_key('_default_install_dir'):
        global _default_install_dir
        _default_install_dir = os.path.normpath(defauts['_default_install_dir'])
        PrintMessage('Default installation directory is ' + _default_install_dir, 2)
    else:
        PrintMessage('Default installation directory missing from config file!', 1)
    
    if defaults.has_key('_deployments_conf'):
        global _deployments_conf
        _deployments_conf = os.path.normpath(defaults['_deployments_conf'])
        PrintMessage('Deployment config file is ' + _deployments_conf, 2)
    else:
        PrintMessage('Deployment config file missing from config file!', 0)
        return False

    if defaults.has_key('_gametypes_dir'):
        global _gametypes_dir
        _gametypes_dir = os.path.normpath(defaults['_gametypes_dir'])
        PrintMessage('Gametypes config directory is ' + _gametypes_dir, 2)
    else:
        PrintMessage('Gametypes config directory missing from config file!', 0)
        return False
    
    return True

def PrintMessage(message, severity):
    if severity > _verbosity:
        pass
    else:
        print message
    
ProcessArgs()
if not ReadConf():
    sys.exit[1]