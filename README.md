# team-local-tactics
A game for the mandatory assignment

Group 20

Members:
 - Endre Sølvberg Tønnessen

## Features
  - Singleplayer
  - Local multiplayer, 1 server and 2 clients.
  - Supports storing champion data in mongoDB.

## Details for assignment

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

## How to run/play
Run program from the top level ``main.py``.
Open three CLI's, start `main.py` in each of them. Choose 1 to be the server, and 2 for clients to play the game. The ``server`` must be started first.

You will be promted with a cli option menu.
```
Welcome to the startup menu for Team Local Tactics!

  Start server   (1)
  Start client   (2)
  Singleplayer   (3)
  Database Setup (4) - (Add champ data to a mongoDB database.  This will delete all previous data.)

  Please choose how to proceed:

> Your input as int
```

### Structure/some details
The server will on startup attempt to retrieve the champions from the MongoDB database. This is done in `mongoDB.py` and `databaseHandler.py` in the `Server` folder.

Should this fail for any reason, it will load champ data from the local .txt file. Allowing the game to continue.

## Errors to look out for
Incase the both server and clients start, and connect correctly. But the hero list is ``empty`` in the clients, this means the server has succesfully connected to the mongoDB, but retrieved an empty result for the hero data. This possibly means that there is no data in the database.

### Database
Should the database for some reason be difficult to setup (it works for me), you can always provide a wrong DB config. It will fail to connect, and then automatically fallback to the local `.txt` with the champion data. 




