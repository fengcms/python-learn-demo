#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint

from core import rest
from core.app import listView, itemView
from core.tool import ok
from config import PREFIX

FIX = PREFIX['fe']

bp = Blueprint('fe', url_prefix=FIX)

# 加载默认 rest 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')

# 将菜单栏目以树形结构输出
@bp.route('tree_channel', methods=['GET'])
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
