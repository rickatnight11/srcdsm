SRCDS Server Manager
====================

Source Dedicated Server (SRCDS) Server Manager can deploy, track, and manage any
number of instances of SRCDS-based games.  It easily scales from single-deployment
to multi-deployment environments and supports any deployment configuration.

Features
--------

SRCDS Server Manager contains the following features:

* Install and manage multiple instances of SRCDS-based games
* Deploy SRCDS installations in any method
	* Single-deployment environments (all games are installed into one SRCDS deployment)
	* Multi-deployment environments (each game is installed into a separate SRCDS deployment)
	* Dynamic-deployment environments (multiple SRCDS deployments, each with one or more games installed) 


Components
------------

This application is currently under initial development, so requirements and configuration is highly subject to change


### srcds.py

This is the main script that performs all tasks including

* Deploy SRCDS
* Install games into SRCDS deployments
* Read/Save Deployment Configuration
* Start/Stop/Track Game Instances

### srcds.conf

This is the configuration file that stores both SRCDS game profiles
and deployment/game profiles. This configuration file can be edited manually,
but ideally the main script (srcds.py) should be used.


Installation
-----------

At this time there are no installation instructions, as the SRCDS Server Manager
consists of only the script and configuration file.  Once the application becomes more robust,
custom deployments per OS distributions will be developed.


Usage
-----

### Deploy SRCDS

To deploy a new installation of SRCDS run use the --deploy switch.  This can be used in several ways:

	srcds.py --deploy
	
This is the minimum amount of syntax required to deploy a new installation of SRCDS.  The script will prompt
for the name and location of the new deployment.

	srcds.py --deploy srcds1
	
If srcds1 is not the name of a currently deployed SRCDS installation, this syntax will deploy a new SRCDS
installation called srcds1 into the current directory.

	srcds.py --deploy srcds1 /path/to/srcds1
	
If srcds1 is not the name of a currently deployed SRCDS installation, this syntax will deploy a new SRCDS
installation called srcds1 into the path provided.


### Install Game

To install a new instance of a game, use the --install switch.  This can be used in several ways:

	srcds.py --install

This is the minimum amount of syntax required to install a new game.  This script will prompt for the
game-type and SRCDS deployment to install the game into.

	srcds.py --install cstrike
	
If this command is run while inside a known SRCDS deployment, the script will install a new instance of
Counter-Strike (or whatever game-type is specified) into that deployment.  Otherwise the script will prompt
for the SRCDS deployment to install an instance of the supplied game-type into.

	srcds.py --install cstrike srcds1
	
If srcds1 is a known SRCDS deployment name, the script will install a new instance of Counter-Strike
(or whatever game-type is specified) into that deployment.

	srcds.py --install cstrike /path/to/srcds1
	
If the provided path is a known SRCDS deployment, the script will install a new instance of Counter-Strike
(or whatever game-type is specified) into that deployment.

### Start a Game

To start a game, use the --start switch.  This can be used in several ways:

	srcds.py --start

If --start switch is used without any arguments, the script will prompt first for which SRCDS deployment
to start a game from and then for which installed game to actually start.

	srcds.py --start cstrike

If a game-type argument is used, the script will prompt for which installed Counter-Strike (or whatever
game-type is specified) should be started.

	srcds.py --start srcds1
	
If a SRCDS deployment name argument is used, the script will prompt for which of the games installed
into that deployment should be started.

	srcds.py --start srcds1 cstrike

If both SRCDS deployment name and game-type arguments are provided, the script will start the game
installed into the provided deployment.

### Stop a Game

To stop a game, use the --stop switch.  This can be used in several ways:

	srcds.py --stop

