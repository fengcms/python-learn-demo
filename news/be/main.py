#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import NotFound
from sanic import Blueprint
import json

import config
from tool import ok, fail, checkParam
from session import makeSession, checkSession, clearSession, updataSession

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

@bp.route('article', methods=['POST', 'GET'])
async def article(request):
    M = request.method
    if M == 'GET':
        res = query.ls('Article')
        if isinstance(res, list):
            return ok(res)
        if res == 404:
            return fail('数据库中没有该表', 404)
        elif res == 500:
            return fail('服务器内部错误', 500)
    elif M == 'POST':
        req = json.loads(request.body)
        res = query.post('Article', req)
        if res == 1:
            return ok('数据添加成功')
        elif res == 404:
            return fail('数据库中没有' + 'Article' + '这个表', 404)
        elif res == 500:
            return fail('数据添加失败')
    else:
        return fail('不被允许的请求方法', 405)

@bp.route('article/<id>', methods=['DELETE', 'GET', 'PUT'])
async def article(request, id):
    M = request.method
    if M == 'GET':
        res = query.get('Article', id)
        if isinstance(res, dist):
            return ok(res)
        elif res == 404:
            return fail('没有查询到数据', 404)
        elif res == 500:
            return fail('服务器内部错误', 500)
    elif M == 'PUT':
        req = json.loads(request.body)
        res = query.put('Article', id, req)
        if res == 1:
            return ok('更新成功')
        elif res == 2:
            return fail('没有这条数据')
        elif res == 3:
            return fail('参数错误')
        elif res == 500:
            return fail('服务器内部错误', 500)
    elif M == 'DELETE':
        res = query.delete('Article', id)
        if res == 1:
            return ok('删除成功')
        elif res == 2:
            return fail('没有这条数据')
        elif res == 500:
            return fail('服务器内部错误', 500)
    else:
        return fail('不被允许的请求方法', 405)


app.blueprint(bp)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=9000)
