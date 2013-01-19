#!/usr/bin/env python

import subprocess

from flask import Flask, request

__EXE = {
    'say': 'cowsay',
    'think': 'cowthink'
}

__ERROR = 'I\'m sorry, what?\n'

def get_cow(message, verb):
    p = subprocess.Popen([__EXE[verb], message],
        shell=False, stdout=subprocess.PIPE)
    return p.communicate()[0]

app = Flask(__name__)

@app.route('/cow/<verb>', methods=['GET'])
def respond(verb='say'):
    if verb in __EXE:
        message = request.args.get('message', '')
        return get_cow(message, verb)
    else:
        return __ERROR

if __name__ == "__main__":
    app.run()
