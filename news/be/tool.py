#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic.response import json
def ok(data):
    return json({"data": data, "status": 0})

def fail(data, status=200):
    return json({"data": data, "status": 1}, status=status)

def checkParam(params, req):
    if not isinstance(params, list):
        return fail('参数错误')
    if not isinstance(req, dict):
        return fail('参数错误')

    for i in params:
        if not i in req:
            return fail('参数错误')

def str2Hump(text):
    arr = text.lower().split('_')
    res = ''
    for i in arr:
        res =  res + i[0].upper() + i[1:]
    return res

