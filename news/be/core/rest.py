#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json

from core import query
from core.tool import ok, fail, str2Hump

def getList (request, name):
    data = json.loads(ls(request, name).body)
    if data['status'] == 0:
        return data['data']
    return 1

def getItem (name, oid):
    data = json.loads(get({}, name, oid).body)
    if data['status'] == 0:
        return data['data']
    return 1

def ls (request, name):
    hmupName = str2Hump(name)
    res = query.ls(hmupName, request)
    if isinstance(res, dict):
        return ok(res['list'], res['total'])
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 503:
        return fail('数据查询失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def post (request, name):
    hmupName = str2Hump(name)
    res = query.post(hmupName, request)
    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 503:
        return fail('数据添加失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def get (request, name, oid):
    hmupName = str2Hump(name)
    res = query.get(hmupName, oid)
    if isinstance(res, dict):
        return ok(res)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 4042:
        return fail('没有这条数据', 404)
    elif res == 4043:
        return fail(name + '数据库中没有数据', 404)
    elif res == 503:
        return fail('数据查询失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def put (request, name, oid):
    hmupName = str2Hump(name)
    res = query.put(hmupName, oid, request)
    if res == 200:
        return ok('更新成功')
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 4042:
        return fail('没有这条数据', 404)
    elif res == 4043:
        return fail(name + '数据库中没有数据', 404)
    elif res == 503:
        return fail('数据更新失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def delete (request, name, oid):
    hmupName = str2Hump(name)
    res = query.delete(hmupName, oid)
    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('您要删除的数据不存在', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 503:
        return fail('数据删除失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)
