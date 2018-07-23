#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import requests
import json
import argparse
from prettytable import PrettyTable

from baidu import baidu 

def checkLang (word):
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
        return [baidu(word, sLang, tLang), sLang]
    else:
        print('Api Error')
        exit()

def fanyi(word, goNext):
    checkRes = checkLang(word)
    res = checkRes[0]
    sLang = checkRes[1]
    if 'trans_result' in res:
        tRes = res['trans_result']
        tableHead = ['原词', word]

        x = PrettyTable(tableHead)
        x.padding_width = 1
        x.align = 'l'

        print('\n\033[1;36m简单结果\033[0m')

        for k, i in enumerate(tRes['data']):
            x.add_row(['结果', i['dst']])
        print(x)

    if 'dict_result' in res:
        dRes = res['dict_result']

        if 'simple_means' in dRes:
            sdRes = dRes['simple_means']

            if 'word_means' in sdRes:
                print('\n\033[1;36m更多翻译\033[0m')
                x = PrettyTable()
                x.header = False
                x.add_row(sdRes['word_means'])
                print(x)

    if goNext:
        print('\n')
        inputWord(False)


def inputWord (isFirst):
    if isFirst:
        print('\n\033[1;36m英汉互译词典\033[0m by FungLeo')
        print('\033[35mTip：退出程序请输入 \033[1;31mexit\033[4;0m\n')
    word = input('请输入要翻译的内容：')
    if word == 'exit':
        print('\033[0m很高兴为您服务')
        exit()
    else:
        fanyi(word, True)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.description='Python 编写的基于百度翻译的命令行翻译工具。支持缀参数直接翻译，如有空格，请用引号包含，或不带参数直接进入连续翻译模式。'
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    parser.add_argument('word', type=str, help='需要翻译的单词', nargs='?')

    args = parser.parse_args()

    if args.word != None:
        fanyi(args.word, False)
    else:
        inputWord(True)
