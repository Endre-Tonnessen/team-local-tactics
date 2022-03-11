# team-local-tactics
A game for the mandatory assignment

Members:
 - Endre Sølvberg Tønnessen


## How to run

Run program from the top level ``main.py``.

You will be promted with a cmd option menu.
```
Welcome to the startup menu for Team Local Tactics!

  Start server   (1)
  Start client   (2)
  Singleplayer   (3)
  Database Setup (4) - (Add champ data to a mongoDB database.  This will delete all previous data.)

  Please choose how to proceed:

> Your input as int
```

For local lan, start one as a ``server``, and two as `clients`. The ``server`` must be started first.

## Technical details for assignment

### Setup

For the mongoDB, you need to set some config options.
If you don't have a `.env` file, you can create one and fill it with the details under
(Alternatively replace the provided `.env.example`)

```py
# Development settings
mongoUsername="username for mongoDB"
password="password for user"
clusterName="name of your cluster"
```

Then, the first time you run the program, the `main.py` in the topmost directory. Choose option 4, initializing the database with correct champion data.

### How to run/play
Open three CLI's, start `main.py` in each of them. Choose 1 to be the server, and 2 for clients to play the game. ! Start the server before the clients. 

### Structure/some details
The server will on startup attempt to retrieve the champions from the MongoDB database. This is done in `mongoDB.py` and `databaseHandler.py` in the `Server` folder.

Should this fail for any reason, it will load champ data from the local .txt file. Allowing the game to continoue.






