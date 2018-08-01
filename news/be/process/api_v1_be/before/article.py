#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import fail, isInt

# async def ls (req):
#     print(req)
#     req['page'] = 1
#     print(req)

async def post (request):
    for i in request['data']:
       if not 'title' in i:
           return fail('标题不能为空', 400)
       elif not 'channel_id' in i:
           return fail('栏目ID不能为空', 400)
       elif not isInt(i['channel_id']):
           return fail('栏目ID只能是数字', 400)
       elif not 'content' in i:
           return fail('文章内容不能为空', 400)

