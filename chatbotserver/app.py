from pymongo import MongoClient
from bson import ObjectId
import uuid
from botModel import model, defaultModel
from flask import Flask, request
import requests 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	ip = getBotIp(request.data.decode('utf-8'))
	if ip != "no":
		code = 200
		url = "http://"+ip+":5001/"
		response = requests.get(url)
		return response.text, code
	else:
		return "not supported domain", 203
	

       
@app.route("/<handler>", methods=['POST'])
def botHandler(handler):
    return response.text

@app.route("/prev", methods=['POST'])
def prev():

    domain = request.json['domain']
    url = "http://"+getBotIp(domain)+":5001/"+request.json['key']
    print(url)
    
    print(request.data.decode('utf-8'))
    response = requests.post(url=url, json=request.json, headers={'Content-type': 'application/json; charset=utf-8'}) 
    return response.text

def getBotIp(domain):
    for bot in botDicts:
        if domain == bot['domain']:
            return bot['botIp']
    return "no"

@app.route("/keys/<key>", methods=['GET'])
def checkKey(key):
    if checkApiKeyInMemory(key):
        response_body = 'ok'
        status = '200'
    else:
        response_body = 'There is no key.'
        status = '303'

    return response_body, status
    
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

def checkApiKeyInMemory(apiKey):
    for bot in botDicts:
        if apiKey == bot['apiKey']:
            return True
    
    return False
        
logonBots = connectLogonBots()
documents = logonBots.find()
botDicts = []

# insertOne(logonBots,defaultModel)


for document in documents:
    botDicts.append(document)

# printAll(logonBots)
app.run(host='0.0.0.0', port=5002)

#printAll(logonBots)
#print(exists(logonBots, 'e26e3e94-2c94-4402-aa44-e6bd24619b55'))
