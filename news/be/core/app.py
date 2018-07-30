#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pkgutil
import os

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.views import HTTPMethodView

from core.tool import fail, query2Dict

from core.process import process

import pre_process
import post_process

from config import PREFIX
import imp

app = Sanic(__name__)

@app.listener('before_server_start')
async def registerModule(app, loop):
    r = 'process/'
    app.process = {}
    o = {}
    a = []
    for i in PREFIX:
        p = '_'.join(list(filter(None, PREFIX[i].split('/'))))
        for d in ['before', 'after']:
            fp = r + p + '/' + d
            if not os.path.exists(fp):
                os.makedirs(fp)
            a.append(fp)

            for x, n, __ in pkgutil.iter_modules([fp]):
                m = None
                m = x.find_module(n).load_module(n)
                print(m)
                #app.process[p+d+n] = m
                o[p+d+n] = m

            #
            # for m in os.listdir(fp):
            #     if m[-3:] == '.py':
            #         # n = m.split('.py')[0]
            #         # fn, path, desc = imp.find_module(n, [fp])
            #         # x = imp.load_module(n, fn, path, desc)
            #         app.process[p+d+n] = x


    #print(app.process)
    print(o)

                    #print(pkgutil.iter_modules(fp))
  #   for i in PREFIX:
  #       # 根据配置前缀，获得对应的前后处理目录
  #       p = '_'.join(list(filter(None, PREFIX[i].split('/'))))
  #       # before = __import__('process.' + p + '.before')
  #       # print(before)
  #       #app[p] = {}
  #       #app[p]['before'] = {}
  #       print(getattr(process, p))
  #       # for _, name, p in pkgutil.iter_modules(process.__path__):
  #       #     print(name)
    # 动态加载前处理模块
    app.pre_process = {}
    for importer, modname, ispkg in pkgutil.iter_modules(pre_process.__path__):
        m = importer.find_module('pre_process.' + modname)\
                .load_module('pre_process.' + modname)
        app.pre_process[modname] = m
    # 动态加载后处理模块
    app.post_process = {}
    for importer, modname, ispkg in pkgutil.iter_modules(post_process.__path__):
        m = importer.find_module('post_process.' + modname)\
                .load_module('post_process.' + modname)
        app.post_process[modname] = m


# 处理 404 页面
@app.exception(NotFound)
def returnNotFound (request, exception):
    return fail(request.url + '没有找到', 404)

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        url = request.url
        request = query2Dict(request.query_string)
        return await process(app, name, request, url, 'ls')
    async def post(self, request, name):
        url = request.url
        request = request.json
        if 'batch_additon' in request and isinstance(request['batch_additon'], list):
            request = {'data': request['batch_additon']}
        else:
            request = {'data': [request]}
        return await process(app, name, request, url, 'post')

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        url = request.url
        request = query2Dict(request.query_string)
        return await process(app, name, request, url, 'get', oid)
    async def put(self, request, name, oid):
        url = request.url
        request = request.json
        return await process(app, name, request, url, 'put', oid)
    async def delete(self, request, name, oid):
        url = request.url
        request = query2Dict(request.query_string)
        return await process(app, name, request, url, 'delete', oid)

