#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok, fail, checkParam, query2Dict

async def ls (request):
    print('前处理参数' + str(request))

async def post (request):
    print('前处理参数' + str(request))
# 
# async def get (request):
#     #return ok('love')
#     return request
