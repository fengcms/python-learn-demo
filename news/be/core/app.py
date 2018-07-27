#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pkgutil

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.views import HTTPMethodView
from sanic import Blueprint

import config
from core.tool import ok, fail, query2Dict
from core.session import checkSession, updataSession

from core import rest
from core import query
from core.process import process

from api import api

import pre_process
import post_process

app = Sanic(__name__)
FIX = config.BE_PREFIX
ANY_API = config.ANONYMOUS_API
KEY_PATH = config.PRIVATE_KEY_PATH

bp = Blueprint('core', url_prefix=FIX)


@app.listener('before_server_start')
async def registerModule(app, loop):
    # 动态加载前处理模块
    app.pre_process = {}
    for importer, modname, ispkg in pkgutil.iter_modules(pre_process.__path__):
        m = importer.find_module('pre_process.' + modname).load_module('pre_process.' + modname)
        app.pre_process[modname] = m
    # 动态加载后处理模块
    app.post_process = {}
    for importer, modname, ispkg in pkgutil.iter_modules(post_process.__path__):
        m = importer.find_module('post_process.' + modname).load_module('post_process.' + modname)
        app.post_process[modname] = m

# 中间件 检查是否登录
@app.middleware('request')
async def checkLogin(request):
    status = True
    url = request.url.split(FIX)[1].split('/')[0]
    for i in ANY_API:
        if i == url:
            status = False
    if status:
        session = request.cookies.get('session')
        cs = checkSession(session)
        if cs == 1:
            return fail('没有权限', 401)
        elif cs == 2:
            return fail('登录超时', 401)
        elif cs == 4:
            return fail('请重新登录', 401)
        elif cs == 0:
            updataSession(session)

# 处理 404 页面
@bp.exception(NotFound)
def returnNotFound (request, exception):
    return fail(request.url + '没有找到', 404)

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        request = query2Dict(request.query_string)
        return await process(app, name, request, 'ls')
    async def post(self, request, name):
        request = request.json
        return await process(app, name, request, 'post')

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        request = query2Dict(request.query_string)
        return await process(app, name, request, 'get', oid)
    async def put(self, request, name, oid):
        request = request.json
        return await process(app, name, request, 'put', oid)
    async def delete(self, request, name, oid):
        request = query2Dict(request.query_string)
        return await process(app, name, request, 'delete', oid)


app.blueprint(bp)
app.add_route(listView.as_view(), FIX + '<name>')
app.add_route(itemView.as_view(), FIX + '<name>/<oid>')
