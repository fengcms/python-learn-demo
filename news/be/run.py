#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from api import be, fe
import config as c
from core.app import app
from core.tool import fail
from core.handle import middleHandle

'''
middleHandle 方法说明：
    1. 用于检查接口请求路径是否合法
    2. 全局检查请求方法是否合法
    3. 可根据提供的白名单或黑名单检查具体请求方法是否合法
    4. 全局是否要求登录
    5. 全局登录则可以设置免登录接口列表

middleHandle(
    request,
    接口前缀, 
    'black' or 'white',     申明名单方法
    名单字典,
    是否全局需登录,         布尔值
    免登录字典
)
'''
# 由于sanic 中间件为全局处理，不支持跟随蓝图独立处理，所以将中间件写在了入口文件中
@app.middleware('request')
async def check(request):
    # 根据请求路径，找到请求对应的接口前缀
    prefix = None
    rep = None
    for i in c.PREFIX:
        if request.headers['host'] + c.PREFIX[i] in request.url:
            prefix = c.PREFIX[i]
    # 处理后台接口中间处理
    if prefix == '/api/v1/be/':
        rep = middleHandle(request, prefix, 'black', c.BLACK_AUTH, True, c.ANONYMOUS_API)
    # 处理前台接口中间处理
    elif prefix == '/api/v1/fe/':
        rep = middleHandle(request, prefix, 'white', c.WHITE_AUTH, False)
    # 处理非法请求地址
    else:
        rep = fail('请求路径不合法', 404, 404)
    # 处理结果为非空，则直接return
    if rep:
        return rep

app.blueprint(fe.bp)
app.blueprint(be.bp)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = c.PORT)
