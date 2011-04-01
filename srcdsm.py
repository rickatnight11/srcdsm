#!/usr/bin/python
""" srcds Server Manager
by Rick White (rickatnight11@gmail.com)
"""

#Imports
import ConfigParser
from optparse import OptionParser

#Variables
_debug = False
_config_file="srcdsm.conf"
_default_install_dir = '/opt/srcds'
users=[]
game_types=[]
servers=[]
processes=[]


def ProcessArgs():
    global _debug
    
    #Define option/argument parser
    parser = OptionParser(usage='usage: %prog [OPTION]', version='%prog 0.1')
    parser.add_option('-d', '--deploy', action='store_true', dest='deploy', help='deploy new installation of SRCDS', default=False)
    parser.add_option('-i', '--install', action='store_true', dest='install', help='install new instance of a game', default=False)
    parser.add_option('-s', '--start', action='store_true', dest='start', help='start a game', default=False)
    parser.add_option('-e', '--stop', action='store_true', dest='stop', help='stop a game', default=False)
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='increase verbosity (enable debug mode)', default=False)
    
        
    (options, args) = parser.parse_args()
    
    #Check for extra arguments
    if len(args) > 0:
        parser.error("too many arguments passed")
    
    #Check for verbosity/debug mode
    if options.verbose:
        _debug = True
    
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
    #Read file into ConfigParser
    try:
        config = open(_config_file, 'r')
        config = ConfigParser.SafeConfigParser()
        config = ConfigParser.SafeConfigParser()
        config.read(_config_file)
    except IOError:
        print 'cannot open', _config_file
        return False
    else:
        if _debug: print "Found Config File (" + _config_file + ")"
    
    
    #Load default variables
    default_items = dict(config.items("DEFAULT"))
    
    
    #Add global processes to processes list
    global_procs = default_items['global_processes'].split(',')
    for proc in global_procs:
        processes.append(proc)
    if _debug: print "Added (" + str(len(global_procs)) + ") processes from global_processes."
    
    #Add global users to users list
    global_users= default_items['global_users'].split(',')
    for user in global_users:
        users.append(user)   
    if _debug: print "Added (" + str(len(global_users)) + ") users from global_users."
    
    #Add games-types to game-types list
    for game_type in config.sections():
        if game_type[:10] == "game-type-":
            game_types.append(dict(config.items(game_type)))

    
    #Add servers to servers list
    for server in config.sections():
        if server[:7] == "server-":
            servers.append(dict(config.items(server)))
    
    #print servers
    
    return 0

ProcessArgs()
ReadConf()