#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, request

import db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news', methods=['GET', 'POST'])
def news():
    print(str(request.form))
    if request.method == 'GET':
        print('get news')
        return 'get status:200'
    elif request.method == 'POST':
        r = request.form
        print(r['title'])
        print(r['content'])
        sql_str = '''INSERT INTO article (title, content) VALUES ('{title}','{content}')'''
        sql_str = sql_str.format(title = r['title'], content = r['content'])
        print(sql_str)
        db.insertDb(sql_str)
        print('post news')
        return 'post status:200'

#@app.route('/news/<username>')
#def news(username):
#    res = 'your username is ' + username
#    return res
#
#@app.route('/id/<int:id>')
#def id(id):
#    print(type(id))
#    res = 'your id is ' + str(id)
#    return res

if __name__ == '__main__':
    app.run()
