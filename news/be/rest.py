#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json

import query
from tool import ok, fail, str2Hump

def ls (request, name):
    hmupName = str2Hump(name)
    res = query.ls(hmupName)
    if isinstance(res, list):
        return ok(res)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 500:
        return fail('服务器内部错误', 500)
    else:
        return fail('未知错误')

def post (request, name):
    hmupName = str2Hump(name)
    req = json.loads(request.body)
    res = query.post(hmupName, req)
    if res == 1:
        return ok('数据添加成功')
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 500:
        return fail('数据添加失败')
    else:
        return fail('未知错误')

def get (request, name, oid):
    hmupName = str2Hump(name)
    res = query.get(hmupName, oid)
    if isinstance(res, dict):
        return ok(res)
    elif res == 404:
        return fail('没有查询到数据', 404)
    elif res == 500:
        return fail('服务器内部错误', 500)
    else:
        return fail('未知错误')

def put (request, name, oid):
    hmupName = str2Hump(name)
    req = json.loads(request.body)
    res = query.put(hmupName, oid, req)
    if res == 1:
        return ok('更新成功')
    elif res == 2:
        return fail('没有这条数据')
    elif res == 3:
        return fail('参数错误')
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 500:
        return fail('服务器内部错误', 500)
    else:
        return fail('未知错误')

def delete (request, name, oid):
    hmupName = str2Hump(name)
    res = query.delete(hmupName, oid)
    if res == 1:
        return ok('删除成功')
    elif res == 2:
        return fail('没有这条数据')
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 500:
        return fail('服务器内部错误', 500)
    else:
        return fail('未知错误')
