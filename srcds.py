#!/usr/bin/python
""" srcds Server Manager
by Rick White (rickatnight11@gmail.com)
"""

_debug=True

import ConfigParser

#Variables
config_file="srcds.conf"
users=[]
game_types=[]
servers=[]
processes=[]

def ReadConf():
    
    #Test for config file
    try:
        config = open(config_file, 'r')
    except IOError:
        print 'cannot open', config_file
    else:
        if _debug: print "Found Config File (" + config_file + ")"
    
    #Read file into ConfigParser
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    
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
    
    print servers
    
    return 0


ReadConf()