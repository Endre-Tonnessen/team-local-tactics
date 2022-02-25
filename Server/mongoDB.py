import pymongo
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv()

print(pymongo.version)

# Get you password from .env file
mongoUsername = os.environ.get("mongoUsername")
password = os.environ.get('password')
clusterName = os.environ.get("clusterName")


# Connect to you cluster
client = MongoClient('mongodb+srv://' + mongoUsername + ':' + password + '@' + clusterName + '.k4xov.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# mongodb+srv://Endre:<password>@cluster0.k4xov.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

# Create a new database in your cluster
database = client.INF142

# Create a new collection in you database
person = database.person

personDocument = {
  "firstname": "Ola",
  "lastname": "Nordmann",
  "course": "INF142"
}

person.insert_one(personDocument)





