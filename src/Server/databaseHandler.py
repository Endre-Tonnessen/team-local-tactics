#!/usr/bin/env python3
from __future__ import annotations
from typing import Dict, List
from .mongoDB import mongoDB
from ..Game.champlistloader import load_some_champs

class databaseHandler:
    def __init__(self) -> databaseHandler:
        self.conn = mongoDB() # Database connection
    
    def getChampions(self) -> List[Dict[str,str]]:
        """ Retrieves Champion data from database """
        champions = self.conn.retrieveData()
        return champions        
    
    def insertChampions(self):
        """ Inserts champion data from 'some_champs.txt' into the database """
        data = load_some_champs()
        champList = []
        for champ in data.values():
            champList.append(
                {
                    "name": champ._name,
                    "rock": champ._rock,
                    "paper": champ._paper,
                    "scissors": champ._scissors
                }
            )
        self.conn.insert(champList)
