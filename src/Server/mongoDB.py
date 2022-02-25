from __future__ import annotations
from ast import List
from typing import Dict
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class mongoDB:
  """  Creates connectino to external database  """
  def __init__(self) -> mongoDB:
    """ Returns database connection """
    #print("Using pymongo version", pymongo.version)
    # Get you password from .env file
    mongoUsername = os.environ.get("mongoUsername")
    password = os.environ.get('password')
    clusterName = os.environ.get("clusterName")

    try:
      # Connect to you cluster
      self.client = MongoClient('mongodb+srv://' + mongoUsername + ':' + password + '@' + clusterName + '.k4xov.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
      # Create a new database in your cluster
      self.database = self.client.INF142
    except Exception as e:
      print(e)
      print("Database connection failed.")
      
  def retrieveData(self) -> List[Dict[str,str]]:
    docu = self.database.champions
    champ = []
    for data in docu.find({},{"_id":0}):
      champ.append(data)
    return champ

  def insert(self, championsDocument):
    """ 
      Inserts given data into the champions document.
    """
    # Create a new collection in you database
    champions = self.database.champions
    champions.insert_many(championsDocument)
    
    



