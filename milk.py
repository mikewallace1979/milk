#!/usr/bin/env python

import subprocess

from flask import Flask, request

__EXE = {
    'say': 'cowsay',
    'think': 'cowthink'
}

__COWS = [
    'beavis.zen',
    'bong',
    'bud-frogs',
    'bunny',
    'cheese',
    'cower',
    'daemon',
    'default',
    'dragon-and-cow',
    'dragon',
    'elephant-in-snake',
    'elephant',
    'eyes',
    'flaming-sheep',
    'ghostbusters',
    'head-in',
    'hellokitty',
    'kiss',
    'kitty',
    'koala',
    'kosh',
    'luke-koala',
    'mech-and',
    'meow',
    'milk',
    'moofasa',
    'moose',
    'mutilated',
    'ren',
    'satanic',
    'sheep',
    'skeleton',
    'small',
    'sodomized',
    'stegosaurus',
    'stimpy',
    'supermilker',
    'surgery',
    'telebears',
    'three-eyes',
    'turkey',
    'turtle',
    'tux',
    'udder',
    'vader-koala',
    'vader',
    'www'
]

__ERROR = 'I\'m sorry, what?\n'

def get_cow(message, verb='say', cowfile='default'):
    if not verb in __EXE:
        raise('Unsupported action')
    if not cowfile in __COWS:
        raise('Unsupported cow')
    p = subprocess.Popen([__EXE[verb], '-f', cowfile, message],
        shell=False, stdout=subprocess.PIPE)
    return p.communicate()[0]

app = Flask(__name__)

@app.route('/cow/<verb>', methods=['GET'])
def cow(verb='say'):
    try:
        message = request.args.get('message', '')
        cowfile = request.args.get('cowfile', 'default')
        return get_cow(message, verb, cowfile)
    except:
        return __ERROR

@app.route('/cows', methods=['GET'])
def list_cows():
    return '%s\n' % '\n'.join(__COWS)

if __name__ == '__main__':
    app.run()
