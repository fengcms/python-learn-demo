#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic.response import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as CPK
import base64
from urllib.parse import unquote
import hashlib

def ok(data, total = None):
    if isinstance(data, list):
        if total != None:
            return json({'data': {'list': data, 'total': total}, 'status': 0})
        else:
            return json({'data': {'list': data}, 'status': 0})
    else:
        return json({"data": data, "status": 0})

def fail(data, statusCode=1, httpCode=200):
    return json({"data": data, "status": statusCode}, status=httpCode)

def checkParam(params, req):
    if not isinstance(params, list):
        return fail('参数错误', 400)
    if not isinstance(req, dict):
        return fail('参数错误', 400)

    for i in params:
        if not i in req:
            return fail('参数错误', 400)

def middleHandle(request, authList = {}, authType = 'black',\
        anyList = {}, checkLogin = True):
    urlArr = request.url.split(FIX)[1].split('?')[0].split('/')
    method = request.method
    apiName = urlArr[0].lower()

    # 检查请求路径是否合法
    if len(urlArr) == 0 or len(urlArr) > 2:
        return fail('请求路径不合法', 404, 404)

    # 全局请求方法检查
    if len(urlArr) == 1 and not method in ['GET', 'POST']:
        return fail('不被允许的请求方法', 405, 405)
    if len(urlArr) == 2 and not method in ['GET', 'PUT', 'DELETE']:
        return fail('不被允许的请求方法', 405, 405)

    # 检查请求方法自定义名单处理
    for i in authList:
        m = 'LS' if len(urlArr) == 1 and method == 'GET' else method
        if apiName == i.lower():
            # 黑名单处理
            if authType == 'black' and m in authList[i]:
                return fail('该请求未被授权', 405, 405)
            # 白名单处理
            if authType == 'white' and not m in authList[i]:
                return fail('该请求未被授权', 405, 405)

    # 检查接口是否在免登陆列表
    noAnyApi = checkLogin
    if noAnApi:
        for i in anyList:
            if apiName == i.lower():
                noAnyApi = False

    # 校验是否登录
    if noAnyApi:
        session = request.cookies.get('session')
        cs = checkSession(session)
        if cs == 1:
            return fail('没有权限', 401, 401)
        elif cs == 2:
            return fail('登录超时', 401, 401)
        elif cs == 4:
            return fail('请重新登录', 401, 401)
        elif cs == 0:
            updataSession(session)

def isInt(num):
    try:
        num = int(str(num))
        return isinstance(num, int)
    except:
        return False

def str2Hump(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    for i in arr:
        res =  res + i[0].upper() + i[1:]
    return res

def query2Dict(text):
    try:
        text = unquote(text)
        obj = dict([i.split('=') for i in text.split('&')]) 
        return obj
    except Exception as e:
        return {}

def rsaEncrypt(keypath, string):
    with open(keypath, 'r') as f:
        pubkey = f.read()
        rsaKey = RSA.importKey(pubkey)
        cipher = CPK.new(rsaKey)
        res = base64.b64encode(cipher.encrypt(string.encode(encoding="utf-8")))
        return res.decode(encoding = 'utf-8')

def rsaDecrypt(keypath, enCode):
    with open(keypath, 'r') as f:
        prikey = f.read()
        rsaKey = RSA.importKey(prikey)
        cipher = CPK.new(rsaKey)
        res = cipher.decrypt(base64.b64decode(enCode), "ERROR")
        return res.decode(encoding = 'utf-8')

def getMd5(source):
    if isinstance(source, str):
        source = source.encode('utf-8')
    m1 = hashlib.md5()
    m1.update(source)
    res = m1.hexdigest()
    return res


