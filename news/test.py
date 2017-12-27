#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news/<username>')
def news(username):
    res = 'your username is ' + username
    return res

@app.route('/id/<int:id>')
def id(id):
    print(type(id))
    res = 'your id is ' + str(id)
    return res

if __name__ == '__main__':
    app.run()
