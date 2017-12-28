#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, request, json
import model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'GET':
        model.readDb()
        return 'get status:200'
    elif request.method == 'POST':
        model.insertDb(request.form.to_dict())
        return 'post status:200'


if __name__ == '__main__':
    app.run()
