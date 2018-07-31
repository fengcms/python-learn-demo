#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pkgutil
import os

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.views import HTTPMethodView

from core.tool import fail, query2Dict

from core.process import doProcess

from config import PREFIX

app = Sanic(__name__)

# 加载前后处理模块
'''
通过遍历 process 文件夹，得到对应接口前缀匹配的模块文件夹
然后遍历其中的 before after 分别找出对应的前后处理内容

注意: process 中的所有文件夹必须包含 __init__.py 文件，否则不会被自动识别为模块
参考目录结构如下:

    process
    ├── __init__.py
    ├── api_v1_be
    │   ├── __init__.py
    │   ├── after
    │   │   ├── __init__.py
    │   │   └── article.py
    │   └── before
    │       ├── __init__.py
    │       └── article.py
    └── api_v1_fe
        ├── __init__.py
        ├── after
        │   ├── __init__.py
        │   └── article.py
        └── before
            ├── __init__.py
            └── article.py
'''
@app.listener('before_server_start')
async def registerModule(app, loop):
    r = 'process'
    app.process = {}
    # 进行第一层循环，加载不同接口前缀对应的模块
    for x, n, _ in pkgutil.iter_modules([r]):
        m = x.find_module(r + '.' + n).load_module(r + '.' + n)
        # 进行第二层循环，加载对应的不同前后处理模块
        for xx, nn, __ in pkgutil.iter_modules([r + '/' + n]):
            mm = xx.find_module(r + '.' + n + '.' + nn).\
                    load_module(r + '.' + n + '.' + nn)
            # 进行第三层循环，加载前后处理的所有响应模块
            for xxx, nnn, ___ in pkgutil.iter_modules([r + '/' + n + '/' + nn]):
                mmm = xxx.find_module(r + '.' + n + '.' + nn + '.' + nnn).\
                        load_module(r + '.' + n + '.' + nn + '.' + nnn)
                # 将得到的结果装载到 app.process 以供全局使用
                app.process[n+nn+nnn] = mmm

# 处理 404 页面
@app.exception(NotFound)
def returnNotFound (request, exception):
    return fail(request.url + '没有找到', 404)

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'ls')
    async def post(self, request, name):
        data = request.json
        if 'batch_additon' in request and isinstance(request['batch_additon'], list):
            request = {'data': request['batch_additon']}
        else:
            request = {'data': [request]}
        return await doProcess(app, name, request, data, 'post')

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'get', oid)
    async def put(self, request, name, oid):
        data = request.json
        return await doProcess(app, name, request, data, 'put', oid)
    async def delete(self, request, name, oid):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'delete', oid)

