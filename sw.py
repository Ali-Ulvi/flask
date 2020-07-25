import os

import flask

from flask import request


class Server:
    def __init__(self):
        self.data = {}

    def run(self):
        app = flask.Flask("AUToSMServer")

        # app.config["DEBUG"] = True

        @app.route('/', methods=['GET'])
        def get():
            if request.args['name'] not in self.data:
                return "No SMS"
            return self.data[request.args['name']]

        @app.route('/set', methods=['GET'])
        def sett():
            val=request.args['value'].rstrip("\\n")
            if val == 'NoSMS':
                self.data[request.args['name']] = val
            elif request.args['name'] in self.data:
                if val == 'NoSMS':
                    self.data[request.args['name']] = val
                else:
                    self.data[request.args['name']] += val
            else:
                self.data[request.args['name']] = val

            return self.data.__repr__()

        if os.environ.get("PORT"):
            host = '0.0.0.0'
        else:
            host = '127.0.0.1'
        app.run(host, port=int(os.environ.get("PORT", 5000)))


Server().run()
