# -*- encoding:utf-8 -*-

import flask

app = flask.Flask(__name__)

@app.route('/')
def helo():
        return "HELLO!!"
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)