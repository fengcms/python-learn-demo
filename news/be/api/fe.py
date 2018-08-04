#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
import json
import re
import hashlib
import os

from core import rest, app
from core.app import listView, itemView
from core.tool import ok, fail, rsaDecrypt, checkParam
from core.handle import middleHandle

from config import PREFIX, PRIVATE_KEY_PATH as KEY_PATH,\
                UPLOAD_PATH, SUPPORT_TYPE, ANONYMOUS_API as ANY_API,\
                WHITE_AUTH

FIX = PREFIX['fe']

bpfe = Blueprint('fe', url_prefix=FIX)

# 加载默认 rest 接口生成路由
bpfe.add_route(listView.as_view(), '<name>')
bpfe.add_route(itemView.as_view(), '<name>/<oid>')

# 中间件 
@bpfe.middleware('request')
async def check(request):
    '''
    middleHandle 方法说明：
        1. 用于检查接口请求路径是否合法
        2. 全局检查请求方法是否合法
        3. 可根据提供的白名单或黑名单检查具体请求方法是否合法
        4. 全局是否要求登录
        5. 全局登录则可以设置免登录接口列表
    middleHandle(request, 接口前缀, 黑白名单字典, 'black' or 'white', 免登录字典, 是否全局需登录)
    '''
    middleHandle(request, FIX, WHITE_AUTH, 'white', {}, False)


# 将菜单栏目以树形结构输出
@bpfe.route('tree_channel', methods=['GET'])
async def tree_channel(request):
    sourceData = rest.getList({'pagesize': -1, 'sort': '-id'}, 'channel')
    if sourceData == 1:
        return fail('服务器内部错误', 500, 500)
    if sourceData['total'] < 1:
        return fail('您当前还没有添加任何栏目')

    sourceList = sourceData['list']

    def makeTree(pid, arr):
        res = []
        for i in arr:
            if i['pid'] == pid:
                rep = makeTree(i['id'], arr)
                if len(rep) != 0:
                    i['children'] = rep
                res.append(i)
        return res
    res = makeTree(0, sourceList)


    return ok(res)
