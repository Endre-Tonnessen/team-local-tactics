#!/usr/bin/env python3
from rich import print
import sys
from src.Game import teamlocaltactics
from src.Server.TNTServer import TNTServer
from src.Client.TNTClient import TNTClient
from src.Server.databaseHandler import databaseHandler


print('\n''\n'
        'Welcome to the [bold green]startup[/bold green] menu for [bold yellow]Team Local Tactics[/bold yellow]!'
        '\n')

print('  Start server   (1)''\n'
      '  Start client   (2)''\n'
      '  Singleplayer   (3)''\n'
      '  Database Setup (4) - (Add champ data to a mongoDB database. [orange1] This will delete all previous data.[/orange1])''\n''\n'
      '  Please choose how to proceed:''\n'
      )

lo = True
while lo:
    match int(sys.stdin.readline()):
        case 1: 
            lo = False
            print('\n')
            server = TNTServer()
        case 2: 
            lo = False
            print('\n')
            client = TNTClient()
        case 3:
            # Starts singleplayer
            lo = False
            print('\n')
            teamlocaltactics.main()
        case 4:
            # Promts database
            try:
                db = databaseHandler()
                db.deleteChampionData()
                db.insertChampions() 
                print("[green] Succesfully initialized database. [/green]")
                print(" Please choose how to proceed:")
            except Exception as e:
                print("[red] An error was raised when inserting champions into MongoDB database.   [/red]")
                print("[red] It is recommended to manually check if the data was correctly added.  [/red]")
           
        case _: print("[orange1]Not a valid option. [/orange1]")
 












