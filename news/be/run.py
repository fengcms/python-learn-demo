#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from api import be, fe
import config as c
from core.app import app
# from core.tool import fail
# from core.handle import middleHandle

# @app.middleware('request')
# async def check(request):
#     prefix = None
#     for i in c.PREFIX:
#         if i in request.url:
#             prefix = c.PREFIX[i]
#     if prefix == '/api/v1/be/':
#         return middleHandle(request, prefix, c.BLACK_AUTH, 'black', c.ANONYMOUS_API, True)
#     elif prefix == '/api/v1/fe/':
#         return middleHandle(request, prefix, c.WHITE_AUTH, 'white', {}, False)
#     else:
#         return fail('请求路径不合法', 404, 404)

app.blueprint(fe.bp)
app.blueprint(be.bp)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = c.PORT)
