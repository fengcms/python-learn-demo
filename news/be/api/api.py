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

from config import PREFIX, PRIVATE_KEY_PATH as KEY_PATH,\
		UPLOAD_PATH, SUPPORT_TYPE, ANONYMOUS_API as ANY_API

FIX = PREFIX['be']

bp = Blueprint('news', url_prefix=FIX)

# 加载默认 rest 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')

# 中间件 检查是否登录
@bp.middleware('request')
async def checkLogin(request):
    status = True
    url = request.url.split(FIX)[1].split('/')[0]
    for i in ANY_API:
        if i == url:
            status = False
    if status:
        session = request.cookies.get('session')
        cs = checkSession(session)
        if cs == 1:
            return fail('没有权限', 401)
        elif cs == 2:
            return fail('登录超时', 401)
        elif cs == 4:
            return fail('请重新登录', 401)
        elif cs == 0:
            updataSession(session)

# 登出处理
@bp.get("logout")
async def logout(request):
    session = request.cookies.get('session')
    res = fail('退出失败', 401)
    cs = checkSession(session)
    if cs == 0:
        clearSession()
        res = ok('退出成功')
    del res.cookies['session']
    return res

# 登录处理
@bp.route("login", methods=['POST'])
async def login(request):
    req = json.loads(request.body)
    checkParam(['account', 'password'], req)
    accRes = json.loads(rest.get({}, 'manages', 'first').body)
    if accRes['status'] == 0:
        acc = accRes['data']
        accPw = rsaDecrypt(KEY_PATH, acc['password'])
        reqPw = rsaDecrypt(KEY_PATH, req['password'])
        reqPwLen = len(reqPw)
        if req['account'] != acc['username']:
            res = fail('用户名不正确')
            del res.cookies['session']
            return res
        elif accPw != reqPw:
            res =  fail('密码不正确')
            del res.cookies['session']
            return res
        elif reqPwLen < 6 or reqPwLen > 16:
            res =  fail('密码长度为 6-16 位')
            del res.cookies['session']
            return res
        else:
            session = makeSession(req['account'])
            res = ok('登录成功')
            res.cookies['session'] = session
            res.cookies['session']['httponly'] = True
            return res
    else:
        return fail('服务器内部错误', 503)

# 网站信息接口特殊处理
@bp.route('site', methods=['POST', 'GET'])
async def site(request):
    M = request.method
    if M == 'GET':
        return rest.get(request, 'site', 'first')
    elif M == 'POST':
        request = json.loads(request.body)
        return rest.put(request, 'site', 'first')
    else:
        return fail('不被允许的请求方法', 405)

# 网站管理员接口特殊处理
@bp.route('manages', methods=['PUT'])
async def manages(request):
    req = json.loads(request.body)
    checkParam(['account', 'old_password', 'new_password'], req)
    oldPw = rsaDecrypt(KEY_PATH, req['old_password'])
    newPw = rsaDecrypt(KEY_PATH, req['new_password'])
    newPwLen = len(newPw)
    if oldPw == newPw:
        return fail('新密码不能与原密码相同')
    if newPwLen < 6 or newPwLen > 16:
        return fail('密码长度不能小于6位或大于16位')
    if not re.match(r'^[a-zA-Z0-9_]+$', newPw):
        return fail('密码只能是大小写字母加数字以及下划线的组合')

    # 获取存储密码
    saveManage = json.loads(rest.get(request, 'manages', 'first').body)['data']
    saveId = saveManage['id']
    savePw = rsaDecrypt(KEY_PATH, saveManage['password'])
    if oldPw != savePw:
        return fail('原密码不正确')

    # 提交密码
    r = {'username': req['account'], 'password': req['new_password']}
    return rest.put(r, 'manages', saveId)

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
