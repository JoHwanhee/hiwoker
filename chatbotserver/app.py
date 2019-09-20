from pymongo import MongoClient
from bson import ObjectId
import uuid
from botModel import model, defaultModel
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def connect():
    username = 'hwanhee'
    password = 'hwanhee'
    return MongoClient('mongodb+srv://%s:%s@cluster0-89apv.mongodb.net/test?retryWrites=true&w=majority' % (username, password))

def getDatabase(connection, dbName):
    return connection[dbName]

def getCollection(db, collectionName):
    return db[collectionName]

def connectLogonBots():
    connection = connect()
    db = getDatabase(connection, 'chatbotsession')
    return getCollection(db, 'logonBots')

def exists(collection, apiKey):
    cursor = collection.find({"apiKey": apiKey})
    return cursor.count() == 1

def insertOne(collection, model):
    if exists(collection, model['apiKey']) == False:
        collection.insert_one(model)
        print(model['apiKey'])

def printAll(collection):
    for result in collection.find():
        print(result)

# logonBots = connectLogonBots()
# insertOne(logonBots, defaultModel)

app.run(host='0.0.0.0', port=8089)

#printAll(logonBots)
#print(exists(logonBots, 'e26e3e94-2c94-4402-aa44-e6bd24619b55'))