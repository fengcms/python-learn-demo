#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
import json
import re

import config
import core.rest
from core.tool import ok, fail, rsaDecrypt, checkParam

FIX = config.BE_PREFIX

KEY_PATH = config.PRIVATE_KEY_PATH

bp = Blueprint('news', url_prefix=FIX)

@bp.route('site', methods=['POST', 'GET'])
async def site(request):
    M = request.method
    if M == 'GET':
        return rest.get(request, 'site', 1)
    elif M == 'POST':
        request = json.loads(request.body)
        return rest.put(request, 'site', 1)
    else:
        return fail('不被允许的请求方法', 405)
@bp.route('manages', methods=['PUT'])
async def manages(request):
    req = json.loads(request.body)
    checkParam(['account', 'old_password', 'new_password'], req)
    oldPw = rsaDecrypt(KEY_PATH, req['old_password'])
    newPw = rsaDecrypt(KEY_PATH, req['new_password'])
    newPwLen = len(newPw)
    if oldPw == newPw:
        return fail('新密码不能与原密码相同')
    if newPwLen < 6 or newPwLen > 16:
        return fail('密码长度不能小于6位或大于16位')
    if not re.match(r'^[a-zA-Z0-9_]+$', newPw):
        return fail('密码只能是大小写字母加数字以及下划线的组合')

    # 获取存储密码
    saveManage = json.loads(rest.get(request, 'manages', 1).body)['data']
    savePw = rsaDecrypt(PRI_K_P, saveManage['password'])
    if oldPw != savePw:
        return fail('原密码不正确')

    # 提交密码
    r = {'username': req['account'], 'password': req['new_password']}
    return rest.put(r, 'manages', 1)
