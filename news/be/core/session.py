#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import hashlib
import time
import os
from core.tool import getMd5

TEMPPATH = 'temp/'

def makeSession (user, session=None):
    t = str(int(time.time()))
    if session == None:
        data = user + t
        session = getMd5(data)
    sessionPath = TEMPPATH + getMd5(user)
    os.system('echo ' + session + ',' + t + ' > ' + sessionPath)
    return user + '|' + session

def checkSession (session):
    tmp = session.split('|')
    user = tmp[0]
    session = tmp[1]
    sessionPath = TEMPPATH + getMd5(user)
    if os.path.exists(sessionPath):
        with open(sessionPath, 'r') as f:
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
    tmp = session.split('|')
    user = tmp[0]
    session = tmp[1]
    o = makeSession(user, session)
