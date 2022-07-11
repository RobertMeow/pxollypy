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
        if request.json['type'] not in ['sync'] and 'object' in request.json and 'chat_id' in request.json['object']:
            if not DB.receive(f"SELECT COUNT(*) FROM conversations WHERE local_id = '{request.json['object']['chat_id']}'"):
                return '-2'
        return Signals.methods[request.json['type']](db=DB, vk=vk, event=request.json) if request.json['type'] in Signals.methods else '-2'
    return 'access denied'


def test():
    return 'ok'


def main():
    app.add_url_rule('/', view_func=Callback, methods=['POST'])
    app.add_url_rule('/test', view_func=test, methods=['GET'])
