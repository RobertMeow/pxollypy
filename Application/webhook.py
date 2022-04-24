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
    if DB.secret_key == request.json['secret_key']:
        return Signals.methods[request.json['type']](db=DB, vk=vk, event=request.json) if request.json['type'] in Signals.methods else '-2'
    return 'access denied'


def test():
    return 'ok'


def main():
    app.add_url_rule('/', view_func=Callback, methods=['POST'])
    app.add_url_rule('/test', view_func=test, methods=['GET'])
