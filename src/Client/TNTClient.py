from queue import Empty, Queue
from socket import socket, AF_INET, SOCK_STREAM, timeout
from threading import Thread
from typing import Dict, List
import ast
from rich import print
from rich.prompt import Prompt
from ..Game.teamlocaltactics import print_available_champs
from ..Game.teamlocaltactics import print_match_summary
from ..Game.champlistloader import _clientParseChamp
from ..Game.core import Champion

class TNTClient:
    def __init__(self) -> None:
        self._messages = Queue()
        self._receiving = True
        self._buffer_size = 2048
        
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(("localhost", 12000))
        Thread(target=self._recv).start()
   
        self.waitForPlayers()
        print("[bright_yellow] Starting game! [/bright_yellow]\n")

        self.champions = self.getChampions()       
         
        self.chooseChampion()
        self.chooseChampion()
        self.chooseChampion()
        self.chooseChampion()
         
        match = self._messages.get() # Match result
        print(match)
        
        # Shutdown
        self._receiving = False
        exit()
        
        
    def waitForPlayers(self):
        """ Waits for all players to join """
        playerUpdate = ""
        while playerUpdate != "Start":
            try:    
                playerUpdate = self._messages.get() 
            except Empty:
                continue
            
            if playerUpdate == "Start":
                break
            print(playerUpdate)

    
    def getChampions(self) -> Dict[str, Champion]:
        champions: List[Dict[str, str]] = eval(self._messages.get()) 
        print_available_champs(_clientParseChamp(champions))
        return champions
        
    def _recv(self):
        """ Waits for 1 message """
        while self._receiving:
            try:
                data = self.sock.recv(2048)
            except timeout:
                pass
            except:
                break
            else:
                if data:
                    self._messages.put(data.decode())
                else:
                    break
        
    def chooseChampion(self):
        """ Allows player to choose champ. """
        re: str = self._messages.get()
        if "OppositePlayer" in re:
            opp = re.split(':')
            print(f"[{opp[1]}]{opp[2]}[/{opp[1]}]: {opp[3]}")
        else:
            data = ast.literal_eval(re) # Eval to dict
            pick: str = self.input_champion(data['player'], data['color'], data['Player1'], data['Player2'])
            self.sock.send(pick.encode())
        
    def input_champion(self, prompt: str,
                   color: str,
                   player1: list[str],
                   player2: list[str]) -> None:

        # Prompt the player to choose a champion and provide the reason why
        # certain champion cannot be selected
        champs = [d['name'] for d in self.champions]

        while True:
            match Prompt.ask(f'[{color}]{prompt}'):
                case name if name not in champs:
                    print(f'The champion {name} is not available. Try again.')
                case name if name in player1:
                    print(f'{name} is already in your team. Try again.')
                case name if name in player2:
                    print(f'{name} is in the enemy team. Try again.')
                case _:
                    return name # Return choosen Champion



