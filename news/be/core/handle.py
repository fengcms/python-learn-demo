#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.session import makeSession, checkSession, clearSession, updataSession
from core.tool import fail

def middleHandle(request, prefix, authType = 'black', authList = {},\
         checkLogin = True, anyList = {}):
    if prefix in request.url:
        urlArr = request.url.split(prefix)[1].split('?')[0].split('/')
        method = request.method
        apiName = urlArr[0].lower()

        # 检查请求路径是否合法
        if len(urlArr) == 0 or len(urlArr) > 2:
            return fail('请求路径不合法', 404, 404)

        # 全局请求方法检查
        if len(urlArr) == 1 and not method in ['GET', 'POST']:
            return fail('不被允许的请求方法', 405, 405)
        if len(urlArr) == 2 and not method in ['GET', 'PUT', 'DELETE']:
            return fail('不被允许的请求方法', 405, 405)

        # 检查请求方法自定义名单处理
        for i in authList:
            m = 'LS' if len(urlArr) == 1 and method == 'GET' else method
            if apiName == i.lower():
                # 黑名单处理
                if authType == 'black' and m in authList[i]:
                    return fail('该请求未被授权', 405, 405)
                # 白名单处理
                if authType == 'white' and not m in authList[i]:
                    return fail('该请求未被授权', 405, 405)

        # 检查接口是否在免登陆列表
        noAnyApi = checkLogin
        if noAnyApi:
            for i in anyList:
                if apiName == i.lower():
                    noAnyApi = False

        # 校验是否登录
        if noAnyApi:
            session = request.cookies.get('session')
            cs = checkSession(session)
            if cs == 1:
                return fail('没有权限', 401, 401)
            elif cs == 2:
                return fail('登录超时', 401, 401)
            elif cs == 4:
                return fail('请重新登录', 401, 401)
            elif cs == 0:
                updataSession(session)
