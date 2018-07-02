#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import json
import timeid

sourceDir = './json'

def getDate(name):
    for i in timeid.TIME:
        if i[0] in name:
            return i[1]
    return '2018-06-29 00:00:00'
def readJson (filPath):
    f = open(filPath, encoding='utf-8')
    data = json.load(f)

    date = getDate(f.name)
    title = repr(data['data']['title']).replace('\\\\', '|').replace("'",'')
    saveTitle = title.replace('/', ':')
    content = data['data']['markdowncontent']
    info = data['data']['description'].replace('\n', '').replace(' ', '').replace('"', "'")\
            .replace('\\', '|')
    tags = data['data']['tags'].split(',')
    cats = data['data']['categories'].split(',')
    
    if content:
        mdFile = open('./markdown/{title}.md'.format(title=saveTitle), 'a+')
        mdFile.write('---\n')
        mdFile.write('title: "' + title + '"\n')
        mdFile.write('date: ' + date + ' +0800\n')
        mdFile.write('lastmod: ' + date + ' +0800\n')
        mdFile.write('author: fungleo\n')
        mdFile.write('preview: "' + info + '"\n')
        mdFile.write('tags: [')
        tagI = 0
        for tag in tags:
            if tagI == 0:
                mdFile.write('"' + tag + '"')
            else:
                mdFile.write(', "' + tag + '"')
            tagI += 1
        mdFile.write(']\n')

        mdFile.write('categories:\n')
        for cat in cats:
            mdFile.write('    - ' + cat + '\n')

        mdFile.write('---\n\n')
        mdFile.write(content)



def findJson ():
    for fil in os.listdir(sourceDir):
        filPath = os.path.join(sourceDir, fil)
        readJson(filPath)

findJson()
#readJson('./json/48211597.json')
