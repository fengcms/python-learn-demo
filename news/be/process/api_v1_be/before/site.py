#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from core import rest
from core.tool import fail

async def ls(request):
    return rest.get({}, 'site', 'first')

async def post(request):
    dat = request['data']
    if len(dat) > 1:
        return fail('站点信息不能更新多条数据', 400, 400)
    return rest.put(dat[0], 'site', 'first')

async def put(request, oid):
    return fail('不被允许的请求方法', 405)

async def delete(request, oid):
    return fail('不被允许的请求方法', 405)
