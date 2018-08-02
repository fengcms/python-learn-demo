#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

async def ls (response):
    for i in response['list']:
        i.pop('password')
    return response
