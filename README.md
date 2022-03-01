# team-local-tactics
A game for the mandatory assignment

Members:
 - Endre Sølvberg Tønnessen


## How to run

Run program from the top level ``main.py``.

You will be promted with a cmd option menu.
```
Welcome to the startup menu for Team Local Tactics!
Please choose how to proceed:

  Start server  (1)
  Start client  (2)
  Singleplayer  (3)

> Your input as int
```

For local lan, start one as a ``server``, and two as `clients`.

## Technical details for assignment

### Structure
The server will on startup attempt to retrieve the champions from the MongoDB database. This is done in `mongoDB.py` and `databaseHandler.py` in the `Server` folder.

If you don't have a `.env` file, you can create one and fill it with the details under

```py
# Development settings
mongoUsername="username for mongoDB"
password="password for user"
clusterName="name of your cluster"
```

Then on line `26` in `TNTServer.py`, uncomment `db.insertChampions()` to repopulate the database with some basic champions. 







