#!/usr/bin/env python

import subprocess

from flask import Flask, request

def get_cow(message):
    p = subprocess.Popen(['cowsay', message],
        shell=False, stdout=subprocess.PIPE)
    return p.communicate()[0]

app = Flask(__name__)

@app.route('/cow/say', methods=['GET'])
def hello():
    if request.method == 'GET':
        message = request.args.get('message', '')
        cow = get_cow(message)
        return cow

if __name__ == "__main__":
    app.run()
