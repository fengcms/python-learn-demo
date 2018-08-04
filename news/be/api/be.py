#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
import json
import re
import hashlib
import os

from core import rest, app
from core.app import listView, itemView
from core.tool import ok, fail, rsaDecrypt, checkParam
from core.session import makeSession, checkSession, clearSession, updataSession
from core.handle import middleHandle

from config import PREFIX, PRIVATE_KEY_PATH as KEY_PATH,\
                UPLOAD_PATH, SUPPORT_TYPE, ANONYMOUS_API as ANY_API,\
                BLACK_AUTH

FIX = PREFIX['be']

bp = Blueprint('be', url_prefix=FIX)

# 加载默认 rest 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')

# 中间件 
@bp.middleware('request')
async def checkLogin(request):
    '''
    middleHandle 方法说明：
        1. 用于检查接口请求路径是否合法
        2. 全局检查请求方法是否合法
        3. 可根据提供的白名单或黑名单检查具体请求方法是否合法
        4. 全局是否要求登录
        5. 全局登录则可以设置免登录接口列表
    middleHandle(request, 接口前缀, 黑白名单字典, 'black' or 'white', 免登录字典, 是否全局需登录)
    '''
    middleHandle(request, FIX, BLACK_AUTH, 'black', ANY_API, True)

# 登出处理
@bp.get("logout")
async def logout(request):
    session = request.cookies.get('session')
    res = fail('退出失败', 401, 401)
    cs = checkSession(session)
    if cs == 0:
        clearSession(session)
        res = ok('退出成功')
    del res.cookies['session']
    return res

# 登录处理
@bp.route("login", methods=['POST'])
async def login(request):

    # 先检查参数是否正确
    req = json.loads(request.body)
    checkParam(['account', 'password'], req)

    # 根据用户名，从数据库中读取管理员信息
    accRes = json.loads(rest.ls({'username': req['account']}, 'manages').body)

    # 判断查询结果是否正常
    if accRes['status'] == 0:

        # 判断是否查到该管理员
        if len(accRes['data']['list']) >= 1:

            # 处理管路员密码
            acc = accRes['data']['list'][0]
            accPw = rsaDecrypt(KEY_PATH, acc['password'])
            reqPw = rsaDecrypt(KEY_PATH, req['password'])
            reqPwLen = len(reqPw)
            if reqPwLen < 6 or reqPwLen > 16:
                res =  fail('密码长度为 6-16 位')
                del res.cookies['session']
                return res
            elif accPw != reqPw:
                res =  fail('密码不正确')
                del res.cookies['session']
                return res
            else:
                session = makeSession(req['account'])
                res = ok('登录成功')
                res.cookies['session'] = session
                res.cookies['session']['httponly'] = True
                return res
        else:
            res = fail('用户名不正确')
            del res.cookies['session']
            return res
    else:
        return fail('服务器内部错误', 503)

# 将菜单栏目以树形结构输出
@bp.route('tree_channel', methods=['GET'])
async def tree_channel(request):
    sourceData = rest.getList({'pagesize': -1, 'sort': '-id'}, 'channel')
    if sourceData == 1:
        return fail('服务器内部错误', 500, 500)
    if sourceData['total'] < 1:
        return fail('您当前还没有添加任何栏目')

    sourceList = sourceData['list']

    def makeTree(pid, arr):
        res = []
        for i in arr:
            if i['pid'] == pid:
                rep = makeTree(i['id'], arr)
                if len(rep) != 0:
                    i['children'] = rep
                res.append(i)
        return res
    res = makeTree(0, sourceList)


    return ok(res)

# 上传文件接口特殊处理
@bp.route('upload', methods=['POST'])
async def upload(request):
    # 字节码转16进制字符串
    def bytes2hex(bytes):
        hexstr = u""
        for i in range(10):
            t = u"%x" % bytes[i]
            if len(t) % 2:
                hexstr += u"0"
            hexstr += t
        return hexstr.lower()

    # 根据16进制字符串获取文件后缀
    def getSuffix(hexStr):
        print(hexStr)
        for i in SUPPORT_TYPE:
            if i in hexStr:
                return SUPPORT_TYPE[i]
        return 400

    # 判断参数是否正确
    if not request.files and not request.files.get('file'):
        return fail('参数错误', 400)
    image = request.files.get('file').body

    # 判断文件是否支持
    imageSuffix = getSuffix(bytes2hex(image))
    if imageSuffix == 400:
        return fail('不支持的文件类型', 400)

    # 组织图片存储路径
    m1 = hashlib.md5()
    m1.update(image)
    md5Name = m1.hexdigest()

    saveDir = UPLOAD_PATH + md5Name[0:2] + '/'
    savePath = saveDir + md5Name[2:] + '.' + imageSuffix
    resPath = '/' + md5Name[0:2] + '/' + md5Name[2:] + '.' + imageSuffix

    # 如果文件夹不存在，就创建文件夹
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # 将文件写入到硬盘
    tempFile = open(savePath, 'wb')
    tempFile.write(image)
    tempFile.close()

    # 给客户端返回结果
    return ok({"path": resPath})
