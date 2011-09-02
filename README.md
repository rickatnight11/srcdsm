Source Dedicated Server Manager (**srcdsm**)
=======================================

**srcdsm** can deploy, track, and manage any number of instances of
**srcds**-based games.  It easily scales from single-deployment to
multi-deployment environments and supports many deployment
configurations.

Features
--------

**srcdsm** provides the following features:

* Install and manage multiple instances of **srcds**-based games
* Deploy **srcds** installations in any method
	* Single-deployment environments (all games are installed into one **srcds** deployment)
	* Multi-deployment environments (each game is installed into a separate **srcds** deployment)
	* Dynamic-deployment environments (multiple **srcds** deployments, each with one or more games installed) 


Components
------------

This application is currently under initial development,
so requirements and configuration are highly subject to change


### srcdsm.py

The main script that performs all tasks including:

* Deploy **srcds** installations
* Install games into **srcds** deployments
* Read/Save Deployment Configuration
* Start/Stop/Track Game Instances

### srcdsm.conf

The configuation file that stores **srcdsm** settings and defaults.  This
configuration file can be edited manually, but ideally the main script
(srcds.py) should be used.

### deployments.conf

The configuration file that stores a list of deployed **srcds** installations
and their settings.

### Gametype Config Files

Each supported **srcds**-based game has a config file containing all relevant
settings and defaults.


Installation
-----------

At this time there are no installation instructions, as **srcdsm** consists of
only the script and configuration files.  Once the script becomes more robust,
OS-specific distributions will be developed.


Basic Usage
-----------

### Deploy **srcds**

Deploy a new installation of **srcds** with the --deploy switch:

	srcdsm.py --deploy [INSTALLATION_NAME] [INSTALLATION_PATH]

The script will prompt for the any options not supplied and without
defaults in the **srcdsm** config depending on the verbosity level.

### Install Game

Install a new instance of a game with the --install switch:

	srcdsm.py --install [GAMETYPE] [INSTALLATION_NAME]

The script will prompt for the any options not supplied depending on
the verbosity level.

### Start a Game

Start a game with the --start switch:

	srcdsm.py --start [GAMETYPE|all] [INSTALLATION_NAME|all]

The script will prompt for any options not supplied with helpful
hints depending on the verbosity level.

Supplying GAMETYPE without supplying INSTALLATION_NAME will result
in the script's prompting for the requested installation and listing
the known deployments containing instances of the specified gametype.

Supplying INSTALLATION_NAME without supplying GAMETYPE will result
in the script's prompting for the requested gametype and listing
the installed gametype instances in the supplied deployment.

Specifying all for either argument will result in the script's
prompting for confirmation, listing all gametype instances that will
be started.  

### Stop a Game

Stop a game with the --stop switch:

	srcdsm.py --stop [GAMETYPE|all] [INSTALLATION_NAME|all]

The arguments work in the same fashion as the --start arguments.

