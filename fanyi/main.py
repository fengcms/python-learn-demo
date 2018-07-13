#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import requests
import json
import random
import hashlib
import argparse
from prettytable import PrettyTable

import config

appid = config.appid
secretKey = config.secretKey


def fanyi (word, goNext, sLang, tLang):
    salt = str(random.randint(32768, 65536))
    sign = appid + word + salt + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    md5Sign = m1.hexdigest()

    queryForm = {
                "appid": appid,
                "from": sLang,
                "to": tLang,
                "q": word,
                "sign": md5Sign,
                "salt": salt
            }
    r = requests.post('http://api.fanyi.baidu.com/api/trans/vip/translate', data=queryForm)
    if r.status_code == 200:
        res = json.loads(r.text)
        if 'trans_result' in res:
            transRes = res['trans_result']
            tableHead = ['中', '英']
            if sLang == 'en':
                tableHead = ['英', '中']

            x = PrettyTable(tableHead)
            x.padding_width = 1

            for i in transRes:
                x.add_row([i['src'], i['dst']])
            print(x)
            if goNext:
                inputWord(False)
            return
        if 'error_code' in res:
            print(res['error_msg'])
    else:
        print('Api Error')

def checkLang (word, goNext):
    langForm = {'query': word}
    r = requests.post('http://fanyi.baidu.com/langdetect', data=langForm)
    if r.status_code == 200:
        res = json.loads(r.text)
        if res['lan'] == 'en':
            sLang = 'en'
            tLang = 'zh'
        else:
            sLang = 'zh'
            tLang = 'en'
        fanyi(word, goNext, sLang, tLang)
    else:
        print('Api Error')

def inputWord (isFirst):
    if isFirst:
        print('Chinese English Dictionary by FungLeo')
        print('Tip：退出程序请输入 exit')
        print('------------------------')
    word = input('请输入要翻译的内容：')
    if word == 'exit':
        print('很高兴为您服务')
        exit()
    else:
        checkLang(word, True)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.description='Python 编写的基于百度翻译的命令行翻译工具'
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    parser.add_argument('word', type=str, help='需要翻译的单词', nargs='?')

    args = parser.parse_args()

    if args.word != None:
        checkLang(args.word, False)
    else:
        inputWord(True)
