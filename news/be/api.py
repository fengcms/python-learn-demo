#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tool import ok, fail

def Api(bp):
    @bp.get('test')
    async def test(request):
        return ok('test')
