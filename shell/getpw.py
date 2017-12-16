#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import argparse
import re

def cutLength(leng, level):
    res = []
    for i in range(level, 1, -1):
        res.append(random.randint(1, leng - sum(res) - i + 1))
    res.append(leng - sum(res))
    random.shuffle(res)
    return res

def makePassword(dists, arr):
    res = []
    for i in range(len(arr)):
        res += random.choices(dists[i], k=arr[i])
    return res

def getPassword(leng, level):
    arr = cutLength(leng,level)

    str1 = '01'
    str2 = '23456789'
    str3 = 'abcdefghijkmnpqrstuvwxyz'
    str4 = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    str5 = '_@!,.:;-=+/?'

    sDist = [str1+str2]
    cDist = [str2,str3,str4]
    dDist = [str2,str3,str4,str5]

    res = []
    if level == 1:
        res = makePassword(sDist,arr)

    if level == 3:
        res = makePassword(cDist,arr)

    if level == 4:
        res = makePassword(dDist,arr)

    random.shuffle(res)
    return ''.join(res)
# 主函数
if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.description='This program is used to generate simple or complex passwords'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    parser.add_argument('length', type=int, help='The length of the password (Default 8)', nargs='?')

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--simple", help="The password is made up of pure numbers", action="store_true")
    group.add_argument("-c", "--commonly", help="The password is made up of numbers and letters (Default)", action="store_true")
    group.add_argument("-d", "--difficult", help="The password is made up of numbers, letters, and punctuation", action="store_true")

    # 获取命令行参数结果
    args = parser.parse_args()

    # 确定密码长度为命令行设置或者默认为8
    length = args.length or 8

    # 如果密码长度小于 4 则提示并退出
    if length < 4:
        parser.print_usage()
        print('error: The password length must be greater than 3')
        exit()
    
    level = 3

    if args.simple:
        level = 1
    if args.difficult:
        level = 4
    
    res = getPassword(length, level)
    print(res)
    exit()
