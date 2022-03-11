from __future__ import annotations
from ast import Str
from typing import Dict, List
from .databaseHandler import databaseHandler
from socket import socket, AF_INET, SOCK_STREAM
from rich import print
from ..Game.teamlocaltactics import print_match_summary
from ..Game.teamlocaltactics import Match
from ..Game.core import *
from ..Game.teamlocaltactics import Team
from ..Game.champlistloader import _clientParseChamp
from ..Game.champlistloader import load_some_champs

class TNTServer:
    space = "[cyan]  -->  [/cyan]"
    
    def __init__(self) -> TNTServer:
        print("[bold cyan] Server started [/bold cyan]")
        # Establish TCP socket
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(("localhost", 12000))
        self.sock.listen(2)
        
        try:
            # Get Champion data from database
            print(f"{TNTServer.space}[cyan] Attempting to retrieve champions from MongoDB. [/cyan]")
            db = databaseHandler()
            champions = db.getChampions()
            print(f"{TNTServer.space}[cyan] Successfully retrieved champions. [/cyan]\n")
        except Exception as e:
            # Should server fail to get data from MongoDB, revert to local backup. 
            print(f"{TNTServer.space}[red] Failed to retrieve champions from MongoDB. [/red]")
            print(f"{TNTServer.space}[red] Have you correctly set up the config? [/red]")
            print(f"{TNTServer.space}[red] Error is: [/red]", e, "\n")
            print(f"{TNTServer.space}[yellow] Reverting to champion data in local txt file. [/yellow]")
            print(f"{TNTServer.space}[yellow] Game should proceed as normal. [/yellow]")
            champions: List[Dict[str, str]] = self.parseToListOfDict(load_some_champs())
        
        # Get all players
        print(f"{TNTServer.space}[cyan] Waiting for players. [/cyan]")
        self.players: List[socket] = [] # Contains each player socket
        self.waitForPlayers(2)
        print(f"{TNTServer.space}[cyan] All players connected! [/cyan]\n")

        #self.sendAll("[bright_yellow] Starting game! [/bright_yellow]")
        self.sendAll("Start")
        
        # Send Champion list to players      
        self.sendAll(str(champions))
        
        print(TNTServer.space, "[cyan]Starting game![/cyan]")
        self.pickChampion()

        print(TNTServer.space, "[cyan]Results: [/cyan]")
        # Simulate
        champs = _clientParseChamp(champions)
        match = Match(
            Team([champs[name] for name in self.player1]),
            Team([champs[name] for name in self.player2])
        )
        match.play()
        # Send results
        matchSummary: Str = print_match_summary(match)
        self.sendAll(matchSummary)

        exit()

    def parseToListOfDict(self, arg: Dict[str, Champion]) -> List[Dict[str,str]]:
        champs = []
        for champ in arg.values():
            di = dict()
            di['name'] = champ._name
            di['rock'] = champ._rock
            di['paper'] = champ._paper
            di['scissors'] = champ._scissors
            champs.append(di)
        return champs
        
    
    def pickChampion(self):
        # Get Player picks
        #self.sendAll("\n [blue] Pick your champion! [/blue] \n")
        self.player1: List[str] = []
        self.player2: List[str] = []
        p1: socket = self.players[0]
        p2: socket = self.players[1]
            
        for i in range(2):
            # Player 1
            d1 = {
                "player": "Player1",
                "color": "red",
                "Player1": self.player1,
                "Player2": self.player2
            }
            p1.send(str(d1).encode())        
            championChoosen: str = p1.recv(4096).decode()
            print(f"{TNTServer.space} [cyan] Player 1 choose {championChoosen} [cyan]")
            self.player1.append(championChoosen)
            p2.send(f"OppositePlayer:red:Player1:{championChoosen}".encode())
            
            # Player 2
            d2 = {
                "player": "Player2",
                "color": "blue",
                "Player1": self.player2,
                "Player2": self.player1
            }
            p2.send(str(d2).encode())
            championChoosen: str = p2.recv(4096).decode()
            print(f"{TNTServer.space} [cyan] Player 2 choose {championChoosen} [cyan]")
            self.player2.append(championChoosen)
            p1.send(f"OppositePlayer:blue:Player2:{championChoosen}".encode())

    def waitForPlayers(self, amount: int):
        """ Server waits until {amount} of players has joined. """
        for _ in range(amount):
            conn, addr = self.sock.accept()
            self.players.append(conn)
            self.updatePlayerCount(amount)
        
    def updatePlayerCount(self, amount: int):
        """ Tells all players how many has joined """
        message = f"{len(self.players)}/{amount} players connected."
        print(f"{TNTServer.space} {message}")
        self.sendAll(message)
            
    def sendAll(self, msg: str):
        for player in self.players:
            player.send(msg.encode())



