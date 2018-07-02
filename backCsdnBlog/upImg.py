#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import imghdr
import requests as req
import json


# 在源目录中找到所有图片并输出为数组
def findImg(sdir):
    res = []
    for f in os.listdir(sdir):
        fp = os.path.join(sdir, f)
        if not os.path.isdir(fp):
            if imghdr.what(fp):
                res.append(fp)
    return res

def upImg ():
    imgs = findImg('./img/')
    for i in imgs:
        files = {'file': ('imgName', open(i, 'rb'), 'image/jpeg')}
        r = req.post('http://localhost:7000/upimg', files=files)
        rJson = json.loads(r.text)
        if rJson['status'] == 0:
            rPath = rJson['data']['path']
            os.system('echo "' + i + '\t' + rPath + '" >> imgDict.txt')
            print('Succ: ' + i + ' | ' + rPath)
        else:
            os.system('echo "' + i + '" >> imgErr.txt')
            print('upErr: ' + i)
        print(i)

upImg()
