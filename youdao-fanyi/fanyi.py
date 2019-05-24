#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import clipboard
import argparse
import random
import hashlib
import json
import signal
from config import APPID, APPKey
from prettytable import PrettyTable

def fanyi(word, goNext):
    baseUrl = 'https://openapi.youdao.com/api'
    salt = str(random.randint(1000000, 9999999))
    sign = APPID + word + salt + APPKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    md5Sign = m1.hexdigest()

    queryFrom = {
            'appKey': APPID,
            'q': word,
            'from': 'auto',
            'to': 'auto',
            'salt': salt,
            'sign': md5Sign,
        }
    r = requests.post(baseUrl, data=queryFrom)
    if r.status_code == 200:
        res = json.loads(r.text)
        if res['errorCode'] == '0':
            showRes(word, res)
            if goNext:
                print('\n')
                inputWord(False)
        else:
            print(res['errorCode'])
            exit()
    else:
        print(r.status_code)
        exit()

def showRes(word, res):
    tableHead = ['原词', word]

    x = PrettyTable(tableHead)
    x.padding_width = 1
    x.align = 'l'

    print('\n\033[1;36m简单结果\033[35m 该结果会自动复制到剪切板\033[0m')

    for i in res['translation']:
        x.add_row(['结果', i])
        clipboard.copy(i)
    print(x)

    if 'basic' in res:
        print('\n\033[1;36m有道词典\033[0m')
        basic = res['basic']

        if 'wfs' in basic:
            wfs = basic['wfs']
            x = PrettyTable(['演化', '结果'])
            x.padding_width = 1
            x.align = 'l'
            for i in wfs:
                x.add_row([i['wf']['name'], i['wf']['value']])
            print(x)

        if 'explains' in basic:
            exps = basic['explains']
            x = PrettyTable(['示例'])
            x.padding_width = 1
            x.align = 'l'
            for i in exps:
                x.add_row([i])
            print(x)

    if 'web' in res:
        print('\n\033[1;36m网络释义\033[0m')
        x = PrettyTable(['相关词汇', '翻译'])
        x.padding_width = 1
        x.align = 'l'
        for i in res['web']:
            x.add_row([i['key'], ', '.join(i['value'])])
        print(x)

def exitFanyi (code, frame):
    print('\n\033[0m很高兴为您服务')
    exit()

def inputWord (isFirst):
    if isFirst:
        print('\n\033[1;36m英汉互译词典\033[0m by FungLeo')
        print('\033[35mTip：退出程序请输入 \033[1;31mexit\033[4;0m\n')
    signal.signal(signal.SIGINT, exitFanyi)
    word = input('请输入要翻译的内容：')
    if word == 'exit':
        print('\033[0m很高兴为您服务')
        exit()
    else:
        fanyi(word, True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'YouDao Fanyi Cli'
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 0.0.1')
    parser.add_argument('word', type = str, help = '需要翻译的单词', nargs = '?')

    args = parser.parse_args()

    if args.word == None:
        inputWord(True)
    else:
        fanyi(args.word, False)
