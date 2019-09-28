from abc import *
from flask import Flask, Response, request, url_for, redirect
import json
import requests 
import sys

class ApiKeyChecker:
    def __init__(self, key):
        self.key = key

    def check(self):
        URL = 'http://127.0.0.1:5000/keys/' + self.key
        response = requests.get(URL) 
        if response.status_code != 200:
            print(response.text)
            sys.exit()

class hiworksBotServer(metaclass=ABCMeta):
    def __init__(self, key):
        self.guides = []
        self.wrapper = None
        self.key = key
        self.wrapper = FlaskAppWrapper('wrap')
        ApiKeyChecker(key).check()

    def setGuides(self, guides):
        self.guides = guides
    
    def addHandler(self, name, handler):
        self.wrapper.add_endpoint(endpoint='/%s' % name, endpoint_name=name, handler=handler, methods=['POST'])

    def run(self, host = '127.0.0.1', port = 5001):
        self.wrapper.add_endpoint(endpoint='/', endpoint_name='init', handler=self.init, methods=['GET'])
        self.wrapper.add_endpoint(endpoint='/prev', endpoint_name='prev', handler=self.prev, methods=['POST'])
        self.wrapper.run(host, port)

    def init(self):
        return self.wrapper.app.response_class(
            response=json.dumps(self.guides, default=lambda o: o.__dict__, sort_keys=True, indent=4),
            status=200,
            mimetype='application/json; charset=utf-8"'
        )

    def prev(self):
        return redirect(url_for(request.json['key']), code=307)

class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)

    def run(self, host, port):
        self.app.run(host, port)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods =None):
        self.app.add_url_rule(endpoint, endpoint_name, handler,methods=  methods)


class GuideToken:
    def __init__(self, key, displayName):
        self.key = key
        self.displayName = displayName
        self.userCommandTokens = []

    @classmethod
    def from_json(cls, data):
        userCommandTokens = list(map(UserCommandToken.from_json, data["userCommandTokens"]))
        return cls(userCommandTokens)

class UserCommandToken:
    def __init__(self, key, displayName):
        self.key = key
        self.displayName = displayName
        self.value = ''
        self.containsVariable = ''
        self.contentOnly = False
        self.canValues = []
        self.allValues = []

    @classmethod
    def from_json(cls, data):
        return cls(**data)