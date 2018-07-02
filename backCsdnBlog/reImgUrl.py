#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import linecache
import requests as req
from io import BytesIO
import json
import os
import imgDict

#mdFile = 'markdown/Atom 编辑器安装 linter-eslint 插件，并配置使其支持 vue 文件中的 js 格式校验.md'
#emdFile = 'markdown/Shell 命令行，写一个自动整理 ~/Downloads/ 文件夹下文件的脚本.md'
# imgFix = 'https://github.com/fengcms/python-learn-demo/tree/master/img-github'
imgFix = 'https://raw.githubusercontent.com/fengcms/articles/master/image'

DICT = imgDict.DICT


def writeFile (i, line, tarFile):
    if i == 0:
        with open(tarFile, 'w+') as f:
            f.write(line)
            f.close()
    else:
        with open(tarFile, 'a') as f:
            f.write(line)
            f.close()

def reImg (line):
    if '![' in line and '](' in line:
        for i in DICT:
            if i[0] in line:
                return '![](' + imgFix + i[1] + ')'
    return line

def saveImg (mdFile):
    mdName = mdFile.replace('markdown/', '').replace('/', ':')
    print(mdName)
    souFile = open('markdown/' + mdName, 'r', encoding="utf-8")
    tarFile = './calcMarkdown/' + mdName
    with souFile as mdTxt:
        i = 0
        for line in mdTxt:
            writeFile(i, reImg(line), tarFile)
            i += 1

def findMdFile ():
    sdir = 'markdown/'
    res = []
    for f in os.listdir(sdir):
        fp = os.path.join(sdir, f)
        if '.md' in fp:
            res.append(fp)

    for i in res:
        saveImg(i)

#saveImg(mdFile)
findMdFile()
