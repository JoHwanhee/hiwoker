import socket
import uuid

def createUUID():
    return str(uuid.uuid4())


model = { "email":"",
          "apiKey":"",
          "botIp":"",
          "isLogon": False }

defaultModel = { "email": "chohh@gabia.com",
                 "apiKey": createUUID(),
                 "botIp": socket.gethostbyname(socket.getfqdn()),
                 "isLogon": True }