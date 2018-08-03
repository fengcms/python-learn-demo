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

def isInt(num):
    try:
        num = int(num)
        return isinstance(num, int)
    except:
        return False

def str2Hump(text):
    arr = text.lower().split('_')
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


