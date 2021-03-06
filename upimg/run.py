#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import json, text, file
from utils import ok, fail
import os, sys
import hashlib
from config import PORT, TOKEN, ALLOWHOST, IMG401, IMG404, SUPPORT_TYPE

app = Sanic()
baseDir = sys.path[0] + '/image/'

# 检查请求地址是否有权限
def checkHost(host):
    for i in ALLOWHOST:
        if i in host:
            return True
    return False

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
    for i in SUPPORT_TYPE:
        if i == hexStr:
            return SUPPORT_TYPE[i]
    return 'error type'


@app.route('/api/v1/upimg', methods=['POST'])
async def upimg(request):
    # 判断用户是否具有上传权限
    if request.headers.get('token') != TOKEN:
        return fail('您没有使用本服务的权限')
    
    # 判断参数是否正确
    if not request.files and not request.files.get('file'):
        return fail('error args')
    image = request.files.get('file').body

    # 判断文件是否支持
    imageSuffix = getSuffix(bytes2hex(image))
    if 'error' in imageSuffix:
        return fail(imageSuffix)
    
    # 组织图片存储路径
    m1 = hashlib.md5()
    m1.update(image)
    md5Name = m1.hexdigest()

    saveDir = baseDir + md5Name[0:2] + '/'
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

@app.route('/api/v1/img', methods=['GET'])
async def img(request):
    host = request.headers.get('referer') or 'ilovethisword'
    args = request.args.get('path') or 'ilovemywife'
    path = baseDir + args
    if not checkHost(host):
        path = baseDir + IMG401

    if not os.path.exists(path):
        path = baseDir + IMG404
    return await file(path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT)
