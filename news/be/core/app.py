#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pkgutil
import os

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.views import HTTPMethodView

from core.tool import fail, query2Dict

from core.process import process as rest

import process

from config import PREFIX

app = Sanic(__name__)

@app.listener('before_server_start')
async def registerModule(app, loop):
    r = 'process/'
    app.process = {}
    for x, n, _ in pkgutil.iter_modules(process.__path__):
        m = x.find_module('process.' + n).load_module('process.' + n)
        for xx, nn, __ in pkgutil.iter_modules([r + n]):
            mm = xx.find_module('process.' + n + '.' + nn).\
                    load_module('process.' + n + '.' + nn)
            for xxx, nnn, ___ in pkgutil.iter_modules([r + n + '/' + nn]):
                mmm = xxx.find_module('process.' + n + '.' + nn + '.' + nnn).\
                        load_module('process.' + n + '.' + nn + '.' + nnn)
                app.process[n+nn+nnn] = mmm

# 处理 404 页面
@app.exception(NotFound)
def returnNotFound (request, exception):
    return fail(request.url + '没有找到', 404)

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        url = request.url
        request = query2Dict(request.query_string)
        return await rest(app, name, request, url, 'ls')
    async def post(self, request, name):
        url = request.url
        request = request.json
        if 'batch_additon' in request and isinstance(request['batch_additon'], list):
            request = {'data': request['batch_additon']}
        else:
            request = {'data': [request]}
        return await rest(app, name, request, url, 'post')

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        url = request.url
        request = query2Dict(request.query_string)
        return await rest(app, name, request, url, 'get', oid)
    async def put(self, request, name, oid):
        url = request.url
        request = request.json
        return await rest(app, name, request, url, 'put', oid)
    async def delete(self, request, name, oid):
        url = request.url
        request = query2Dict(request.query_string)
        return await rest(app, name, request, url, 'delete', oid)

