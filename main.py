#!/usr/bin/env python3
from src.Server.databaseHandler import *
from rich import print
import sys
from src.Game import teamlocaltactics
from src.Server.TNTServer import TNTServer
from src.Client.TNTClient import TNTClient

print('\n'
        'Welcome to the [bold green]startup[/bold green] guide for [bold yellow]Team Local Tactics[/bold yellow]!'
        '\n'
        'Please choose how to proceed:'
        '\n')

print('  Start server  (1)''\n'
      '  Start client  (2)''\n'
      '  Singleplayer  (3)''\n'
      )

lo = True
while lo:
    match int(sys.stdin.readline()):
        case 1: 
            lo = False
            server = TNTServer()
        case 2: 
            lo = False
            client = TNTClient()
        case 3:
            # Starts singleplayer
            lo = False
            teamlocaltactics.main()
        case _: print("[orange1]Not a valid option. [/orange1]")
 












