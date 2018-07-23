#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import hashlib
import time
import os

TEMPFILE = '__temp__session__'

def makeSession (user):
    t = str(int(time.time()))
    data = user + t
    m1 = hashlib.md5()
    m1.update(data.encode('utf-8'))
    session = m1.hexdigest()
    os.system('echo ' + session + ',' + t + ' > ' + TEMPFILE)
    return session

def checkSession (session):
    if os.path.exists(TEMPFILE):
        with open(TEMPFILE, 'r') as f:
            saveText = str(f.read()).split(',')
            saveSession = saveText[0]
            saveTime = int(saveText[1])
            nowTime = int(time.time())
            if session != saveSession:
                return 1
            elif (nowTime - saveTime) > 3600:
                return 2
            else:
                return 0

    else:
        return 4

def clearSession ():
    os.system('rm ' + TEMPFILE)

def updataSession (session):
    t = str(int(time.time()))
    os.system('echo ' + session + ',' + t + ' > ' + TEMPFILE)
