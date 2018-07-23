#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import NotFound
from sanic.views import HTTPMethodView
from sanic import Blueprint
import json

import config
from tool import ok, fail, checkParam, str2Hump
from session import makeSession, checkSession, clearSession, updataSession

import rest
import query

app = Sanic(__name__)
FIX = config.BE_PREFIX
ANY_API = config.ANONYMOUS_API
bp = Blueprint('v1', url_prefix=FIX)

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

# 登出处理
@bp.get("logout")
async def logout(request):
    session = request.cookies.get('session')
    res = fail('退出失败', 401)
    cs = checkSession(session)
    if cs == 0:
        clearSession()
        res = ok('退出成功')
    del res.cookies['session']
    return res

# 登录处理
@bp.route("login", methods=['POST'])
async def login(request):
    req = json.loads(request.body)
    checkParam(['account', 'password'], req)
    session = makeSession(req['account'])
    res = ok('登录成功')
    res.cookies['session'] = session
    res.cookies['session']['httponly'] = True
    return  res

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        return rest.ls(request, name)
    async def post(self, request, name):
        return rest.post(request, name)

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        return rest.get(request, name, oid)
    async def put(self, request, name, oid):
        return rest.put(request, name, oid)
    async def delete(self, request, name, oid):
        return rest.delete(request, name, oid)


app.blueprint(bp)
app.add_route(listView.as_view(), FIX + '<name>')
app.add_route(itemView.as_view(), FIX + '<name>/<oid>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=9000)
