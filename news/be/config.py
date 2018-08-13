#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

PREFIX = {
    'be': '/api/v1/be/',
    'fe': '/api/v1/fe/',
}

ANONYMOUS_API = ['login', 'logout', 'test']

DB_CONN = 'sqlite:///' + sys.path[0] + '/db/news.db'
# DB_CONN = 'mysql+mysqlconnector://root:123456@localhost:3306/news'

PUBLIC_KEY_PATH = './key/public.pem'
PRIVATE_KEY_PATH = './key/private.pem'

UPLOAD_PATH = './upload/'
SUPPORT_TYPE = {
    'ffd8ffe':'jpg',
    '89504e470d0a1a0a0000':'png',
    '474946383961':'gif',
}

PORT = 9000
PAGESIZE = 10

BLACK_AUTH = {
    'login': ['LS', 'GET', 'PUT', 'DELETE'],
    'site': ['GET', 'PUT', 'DELETE'],
}

WHITE_AUTH = {
    'article': ['LS', 'GET'],
    'channel': ['LS', 'GET'],
    'site': ['LS', 'GET'],
    'manages': [],
    'tree_channel': ['LS'],
}
