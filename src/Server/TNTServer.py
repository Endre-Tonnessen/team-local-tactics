from __future__ import annotations
import pickle
from typing import List
from .databaseHandler import databaseHandler
from socket import socket, AF_INET, SOCK_STREAM
from rich import print
import sys

class TNTServer:
    space = "[cyan]  -->  [/cyan]"
    
    def __init__(self) -> TNTServer:
        print("[bold cyan] Server started [/bold cyan]")
        # Establish TCP socket
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(("localhost", 12000))
        self.sock.listen(2)
        
        # Get Champion data from database
        print(f"{TNTServer.space}[cyan] Attempting to retrieve champions. [/cyan]")
        db = databaseHandler()
        #db.insertChampions() # Uncomment to populate the mongoDB
        champions = db.getChampions()
        print(f"{TNTServer.space}[cyan] Successfully retrieved champions. [/cyan]\n")
        
        # Get all players
        print(f"{TNTServer.space}[cyan] Waiting for players. [/cyan]")
        self.players: List[socket] = [] # Contains each player socket
        self.waitForPlayers(2)
        print(f"{TNTServer.space}[cyan] All players connected! [/cyan]\n")

        #self.sendAll("[bright_yellow] Starting game! [/bright_yellow]")
        self.sendAll("Start")
        
        sys.stdin.readline()

        # Send Champion list to players      
        self.sendAll(str(champions))
        
        print(TNTServer.space, "[cyan]Starting game![/cyan]")

        """ 
        ITS RACE CONDITIONS
        
        FIGURE OUT THREAD SHIT
        
        """


        #THIS SHIT WACK YO
        #self.pickChampion()

        # Simulate
        
        # Send results
        
        sys.stdin.readline()
        
        
    def pickChampion(self):
        # Get Player picks
        self.sendAll("Pick your champion!")
        player1: List[str] = []
        player2: List[str] = []
        
        for i in range(1):
            # Player 1
            p1: socket = self.players[0]
            d1 = {
                "player": "Player1",
                "color": "red",
                "Player1": player1,
                "player2": player2
            }
            p1.send(str(d1).encode())
            championChoosen: str = self.sock.recv(4096).decode()
            player1.append(championChoosen)
            sys.stdin.readline()
            
            # Player 2


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








