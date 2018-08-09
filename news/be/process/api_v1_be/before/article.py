#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import fail, isInt, filterHtml
import markdown

# async def ls (req):
#     print(req)
#     req['page'] = 1
#     print(req)

async def post (request):
    for i in request['data']:
        # 判断必填字段 
        if not 'title' in i:
            return fail('标题不能为空', 400)
        elif not 'channel_id' in i:
            return fail('栏目ID不能为空', 400)
        elif not isInt(i['channel_id']):
            return fail('栏目ID只能是数字', 400)
        elif not 'edit_type' in i:
            return fail('编辑器类别不能为空', 400)
        elif i['edit_type'] != 'html' and i['edit_type'] != 'md':
            return fail('编辑器类别指定错误', 400)

        # 根据编辑器类别，输出文章内容
        if i['edit_type'] == 'md':
            if not 'markdown' in i:
                return fail('文章内容不能为空', 400)
            # 转化markdown格式
            i['content'] = markdown.markdown(i['markdown'])

        if i['edit_type'] == 'html':
            if not 'content' in i:
                return fail('文章内容不能为空', 400)

        # 如果没有传入简介信息，则根据文章内容截取
        if i.get('description') == None or i.get('description') == '':
            i['description'] = filterHtml(i['content'])[0:200].replace('\n', '')

        
