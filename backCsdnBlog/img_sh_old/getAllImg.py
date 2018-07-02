#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import linecache
import requests as req
from io import BytesIO
import json
import os

# mdFile = 'markdown/Atom 编辑器安装 linter-eslint 插件，并配置使其支持 vue 文件中的 js 格式校验.md'

def saveImg (mdFile):
    print(mdFile)
    with open(mdFile, 'r', encoding="utf-8") as mdTxt:
        for line in mdTxt:
            lin = line.replace(' ','').replace('\t', '')
            if lin[0:2] == '![':
                imgUrl = lin.split('(')[1].split(')')[0]
                print('\t' + imgUrl)
                os.system('echo "' + imgUrl + '" >> imgOldUrl.txt')

                # img = BytesIO(req.get(imgUrl).content)
                # files = {'file': ('imgName', img, 'image/jpeg')}
                # r = req.post('http://localhost:7000/upimg', files=files)
                # rJson = json.loads(r.text)
                # if rJson['status'] == 0:
                #     rPath = rJson['data']['path']
                #     os.system('echo "' + imgUrl + '\t' + rPath + '" >> imgDict.txt')
                #     print('Succ: ' + rPath)
                # else:
                #     os.system('echo "' + imgUrl + '" >> imgErr.txt')
                #     print('Err: ' + imgUrl)

def findMdFile ():
    sdir = './markdown/'
    res = []
    for f in os.listdir(sdir):
        fp = os.path.join(sdir, f)
        if '.md' in fp:
            res.append(fp)

    for i in res:
        saveImg(i)

findMdFile()
