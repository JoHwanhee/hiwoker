import socket
import uuid

def createUUID():
    return str(uuid.uuid4())


model = { "email":"",
          "domain": "",
          "apiKey":"",
          "botIp":"",
          "isLogon": False }

defaultModel = { "email": "jhh0220@jhh0220.onhiworks.com",
                 "domain" : "jhh0220.onhiworks.com",
                 "apiKey": createUUID(),
                 "botIp": socket.gethostbyname(socket.getfqdn()),
                 "isLogon": True }