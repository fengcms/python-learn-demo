#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok
from core import rest
import json

import inspect
from config import PREFIX

async def process(app, name, request, url, method, oid=None):
    for i in PREFIX:
        if i in url:
            p = '_'.join(list(filter(None, PREFIX[i].split('/'))))
    
    bm = p + 'before' + name
    am = p + 'after' + name

    if dir(app.process[bm]).count(method) == 1:
        request = await getattr(app.process.get(bm), method)(request)
        if not isinstance(request, dict):
            return request
    # 得到查询结果
    if oid == None:
        response = getattr(rest, method)(request, name)
    else:
        response = getattr(rest, method)(request, name, oid)
    resBody = json.loads(response.body)
    resStatus = response.status
    # 根据返回结果判断是否需要后处理(错误状态就不处理了)
    if resStatus == 200 and resBody['status'] == 0:
        if dir(app.process.get(am)).count(method) == 1:
            data = await getattr(app.process.get(am), method)(resBody['data'])
            return ok(data)
        else:
            return response
    else:
        return response

