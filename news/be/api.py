#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint

import config
from tool import ok, fail

FIX = config.BE_PREFIX
bp = Blueprint('test', url_prefix=FIX)

@bp.get('test')
async def test(request):
    return ok('test')
