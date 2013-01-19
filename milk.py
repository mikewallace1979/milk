#!/usr/bin/env python

import subprocess

from flask import Flask, request

__EXE = {
    'say': 'cowsay',
    'think': 'cowthink'
}

__ERROR = 'I\'m sorry, what?'

def get_cow(message, verb):
    p = subprocess.Popen([__EXE[verb], message],
        shell=False, stdout=subprocess.PIPE)
    return p.communicate()[0]

app = Flask(__name__)

@app.route('/cow/say', methods=['GET'])
def say():
    if request.method == 'GET':
        message = request.args.get('message', '')
        cow = get_cow(message, 'say')
        return cow
    else:
        return __ERROR

@app.route('/cow/think', methods=['GET'])
def think():
    if request.method == 'GET':
        message = request.args.get('message', '')
        cow = get_cow(message, 'think')
        return cow
    else:
        return __ERROR

if __name__ == "__main__":
    app.run()
