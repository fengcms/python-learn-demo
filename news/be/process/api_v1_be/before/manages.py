#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re
from core.rest import getList, getItem
from core.tool import fail, checkParam, rsaDecrypt
from config import PRIVATE_KEY_PATH as KEY_PATH

async def post(request):
    data = request['data']
    for i in data:
        account = i['account']
        # 检查添加的用户名在数据库中是否存在
        saveData = getList({'username': account}, 'manages')
        if saveData != 1 and saveData['total'] >= 1:
            return fail('数据库已有用户名为' + account + '的管理员', 400)
        # 数据库存储字段名为 username 所以这里要改名
        i['username'] = i.pop('account')

async def put(request, oid):
    # 检查必填参数
    checkParam(['account', 'old_password', 'new_password'], request)

    # 检查密码是否符合要求
    oldPw = rsaDecrypt(KEY_PATH, request['old_password'])
    newPw = rsaDecrypt(KEY_PATH, request['new_password'])
    newPwLen = len(newPw)
    if oldPw == newPw:
        return fail('新密码不能与原密码相同')
    if newPwLen < 6 or newPwLen > 16:
        return fail('密码长度不能小于6位或大于16位')
    if not re.match(r'^[a-zA-Z0-9_]+$', newPw):
        return fail('密码只能是大小写字母加数字以及下划线的组合')

    # 检查原密码和数据库存储密码是否一致
    saveManage = getItem('manages', oid)
    savePw = rsaDecrypt(KEY_PATH, saveManage['password'])
    if oldPw != savePw:
        return fail('原密码不正确')

    # 检查用户名是否被修改
    account = request['account']
    if account != saveManage['username']:
        return fail('用户名不能被修改')

    # 将参数整理为数据库所需字段
    request['username'] = request.pop('account')
    request['password'] = request.pop('new_password')
    request.pop('old_password')

async def delete(request, oid):
    # 如果要删除的ID的长度，大于或数据库中所有管理员的条数，则不允许删除
    # 因为必须保证系统中有至少一个管理员
    idLen = len(oid.split(','))
    saveData = getList({'pagesize': -1}, 'manages')
    if saveData != 1 and idLen >= saveData['total']:
        return fail('你不能删除所有管理员', 400)
