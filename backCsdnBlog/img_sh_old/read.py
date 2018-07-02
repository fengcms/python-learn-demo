#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import json

sourceDir = './json'


def readJson (filPath):
    f = open(filPath, encoding='utf-8')
    data = json.load(f)
    
    title = data['data']['title'].replace('/', ':')
    #.replace('~', '～')
    content = data['data']['markdowncontent']
    tags = data['data']['tags'].split(',')
    print(filPath)
    
    if content:
        mdFile = open('''./markdown/{title}.md'''.format(title=title), 'a+')
        mdFile.write('title: ' + title + '\n')
        mdFile.write('date: 2018-06-29 00:00:00 +0800\n')
        mdFile.write('update: 2018-06-29 00:00:00 +0800\n')
        mdFile.write('author: fungleo\n')
        mdFile.write('tags:\n')
        for tag in tags:
            mdFile.write('    -' + tag + '\n')

        mdFile.write('---\n\n')
        mdFile.write(content)



def findJson ():
    for fil in os.listdir(sourceDir):
        filPath = os.path.join(sourceDir, fil)
        readJson(filPath)

findJson()
#readJson('./json/48211597.json')
