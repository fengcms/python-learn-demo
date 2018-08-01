#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok, fail, checkParam, query2Dict

async def ls (response):
    for i in response['list']:
        i.pop('content')
    return response
