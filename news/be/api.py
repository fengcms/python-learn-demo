#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
import json

import config
import rest
from tool import ok, fail

FIX = config.BE_PREFIX
bp = Blueprint('test', url_prefix=FIX)

@bp.route('site', methods=['POST', 'GET'])
async def site(request):
    M = request.method
    if M == 'GET':
        return rest.get(request, 'site', 1)
    elif M == 'POST':
        return rest.put(request, 'site', 1)
    else:
        return fail('不被允许的请求方法', 405)
@bp.route('manages', methods=['PUT'])
async def manages(request):
    oldManage = json.loads(rest.get(request, 'manages', 1).body)['data']
    # oldAccount = oldManage['username']
    oldPassword = oldManage['password']
    print(oldPassword)
    return ok('ok')
