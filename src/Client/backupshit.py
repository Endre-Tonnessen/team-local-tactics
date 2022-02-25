import sys
from socket import socket, AF_INET, SOCK_STREAM
from typing import Dict, List
from rich import print
from rich.prompt import Prompt
from ..Game.teamlocaltactics import print_available_champs
from ..Game.champlistloader import _clientParseChamp
from ..Game.core import Champion

class TNTClient:
    def __init__(self) -> None:
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(("localhost", 12000))
   
        self.waitForPlayers()
        print("[bright_yellow] Starting game! [/bright_yellow]\n")

        self.champions = self.getChampions()       
         
        #THIS SHIT WACK YO
        #self.chooseChampion() 
        sys.stdin.readline()
        
        
    def waitForPlayers(self):
        """ Waits for all players to join """
        while playerUpdate:=self.sock.recv(4096).decode() != "Start":
            if playerUpdate != True:
                print(playerUpdate)

    
    def getChampions(self) -> Dict[str, Champion]:
        champions: List[Dict[str, str]] = eval(self.sock.recv(4096).decode())
        print_available_champs(_clientParseChamp(champions))
        return champions
        
        
        
        ############################

    def chooseChampion(self):
        re = self.sock.recv(4096).decode()
        print(re)
        data = eval(re)
        pick: str = self.input_champion(data['player'], data['color'], data['Player1'], data['Player2'])
        self.sock.send(pick.encode())
        
    def input_champion(self, prompt: str,
                   color: str,
                   player1: list[str],
                   player2: list[str]) -> None:

        # Prompt the player to choose a champion and provide the reason why
        # certain champion cannot be selected
        while True:
            match Prompt.ask(f'[{color}]{prompt}'):
                case name if name not in self.champions:
                    print(f'The champion {name} is not available. Try again.')
                case name if name in player1:
                    print(f'{name} is already in your team. Try again.')
                case name if name in player2:
                    print(f'{name} is in the enemy team. Try again.')
                case _:
                    return name # Return choosen Champion



