#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse
import os
import json

def readJson(path):
    if os.path.exists(path):
        f = open(path)
        jsonTxt = f.read()
        try:
            jsonDitc = json.loads(jsonTxt)
            f.close()
            return jsonDitc
        except:
            print('json文件格式有误')
            f.close()
            exit()
    else:
        print('json文件不存在！')
        exit()

def formatJson(jsonDict, method):
    res = ''
    if method == 'format':
        res = json.dumps(jsonDict, indent = 4,sort_keys=True)
    else:
        res = json.dumps(jsonDict)
    return res

def saveJson(jsonStr, savePath):
    f = open(savePath, 'w')
    f.write(jsonStr)
    f.close()
    print('json 文件保存成功，保存地址: ' + savePath)

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.description='json 格式化和压缩工具，可直接在命令行内输出结果或将结果保存到指定路径。'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    parser.add_argument('jsonFilePath', help='需要处理的json文件路径')
    parser.add_argument('-c', "--compress", help='压缩json，默认为格式化', action="store_true")
    parser.add_argument('-s', "--save", help='是否保存处理后的结果，如不指定保存路径，将覆盖源文件保存。', action="store_true")
    parser.add_argument('savePath', help='处理结果保存路径，如输入该参数，不指定-s参数也可运行。', nargs='?')
    args = parser.parse_args()

    method = 'format'
    if args.compress:
        method = 'compress'

    sPath = args.jsonFilePath
    jsonDict = readJson(sPath)
    jsonStr = formatJson(jsonDict, method)

    isSave = False
    savePath = ''

    if args.save and args.savePath == None:
        isSave = True
        savePath = sPath
    elif args.savePath:
        isSave = True
        savePath = args.savePath

    if isSave:
        saveJson(jsonStr, savePath)
    else:
        print(jsonStr)

    exit()
