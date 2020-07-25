import os

import flask

from flask import request


class Server:
    def __init__(self):
        self.data = {}
        self.observers = []
        self.on = False

    def run(self):
        app = flask.Flask("AUToSMServer")

        # app.config["DEBUG"] = True

        @app.route('/', methods=['GET'])
        def home():
            return self.data[request.args['name']]

        @app.route('/set', methods=['GET'])
        def sett():
            self.data[request.args['name']] = request.args['value']
            return self.data.__repr__()

        if os.environ.get("PORT"):
            host = '0.0.0.0'
        else:
            host = '127.0.0.1'
        self.on = True
        app.run(host, port=int(os.environ.get("PORT", 5000)))


Server().run()