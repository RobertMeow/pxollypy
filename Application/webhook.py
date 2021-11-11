from flask import Flask, request

from .methods import Signals
from .utils.db import ControlDatabase
from .utils.API import API, ErrorVK

app = Flask(__name__)
DB = ControlDatabase()
try:
    vk = API(token=DB.token)
except ErrorVK:
    DB.update_config()
    vk = API(token=DB.token)


def Callback():
    print(request.json)
    if DB.secret_key == request.json['secret_key']:
        return Signals.methods[request.json['type']](db=DB, vk=vk, event=request.json) if request.json['type'] in Signals.methods else -2
    return 'access denied'


def main():
    app.add_url_rule('/', view_func=Callback, methods=['POST', 'GET'])
