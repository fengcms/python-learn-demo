#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

BE_PREFIX = '/api/v1/be/'
FE_PREFIX = '/api/v1/fe/'
ANONYMOUS_API = ['login', 'logout', 'test']

DB_CONN = 'sqlite:///' + sys.path[0] + '/db/news.db'

PUBLIC_KEY_PATH = './key/public.pem'
PRIVATE_KEY_PATH = './key/private.pem'

PORT = 9000
