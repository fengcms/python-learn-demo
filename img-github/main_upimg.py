#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import json, text, file
import os, sys
import hashlib
from PIL import Image
from io import BytesIO

app = Sanic()
baseDir = '/Users/fungleo/Documents/FungLeo/articlesImage/'

# 成功以及失败的返回脚本
def ok(data):
    return json({"data": data, "status": 0})

def fail(data):
    return json({"data": data, "status": 1})

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
    SUPPORT_TYPE = {
            'ffd8ffe':'jpg',
            '3c73766720786d6c6e73':'svg',
            '89504e470d0a1a0a0000':'png',
            '474946383961':'gif',
        }
    for i in SUPPORT_TYPE:
        if i in hexStr:
            return SUPPORT_TYPE[i]
    return 'error type'

def pushGithub():
    os.system('whoami')
    # os.system('cd ' + baseDir + ' & git add -A & git commit -m "pushImage" & git push')
    os.system('cd ' + baseDir)
    os.system('git add -A')
    os.system('git commit -m pushImage')
    os.system('git push')

def saveImage(savePath, image):
    tempFile = open(savePath, 'wb')
    tempFile.write(image)
    tempFile.close()
    pushGithub()


app.static('/gui', './gui')

# 上传文件接口
@app.route('/upimg', methods=['POST'])
async def upimg(request):
    
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
    saveSourcePath = saveDir + md5Name[2:] + '_source.' + imageSuffix
    resPath = '/' + md5Name[0:2] + '/' + md5Name[2:] + '.' + imageSuffix
    print(savePath)
    if imageSuffix == 'svg':
        resPath += '?sanitize=true'


    # 如果文件夹不存在，就创建文件夹
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # 如果是 jpg 图片，则添加水印
    if imageSuffix == 'jpg':
        bImg = BytesIO(image)
        img = Image.open(bImg)
        imgW = img.size[0]
        imgH = img.size[1]

        if imgW >= 300 and imgH >= 100:
            mark = Image.open("mark.png")
            layer = Image.new('RGBA', img.size, (0,0,0,0))
            layer.paste(mark, (imgW - 180, imgH - 60))
            out = Image.composite(layer, img, layer)
            out.save(savePath, 'JPEG', quality = 100)
            # 保存原图
            smark = Image.open("do.png")
            slayer = Image.new('RGBA', img.size, (0,0,0,0))
            slayer.paste(smark, (0, 0))
            sout = Image.composite(slayer, img, slayer)
            sout.save(saveSourcePath, 'JPEG', quality = 100)
        else:
            saveImage(savePath, image)

    # 否则直接将文件写入到硬盘
    else:
        saveImage(savePath, image)

    # 给客户端返回结果
    return ok({"path": resPath})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7000)
