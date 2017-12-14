#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import argparse
import re

# 用字典和长度随机生成一个密码
def passwordMaker(leng, dicts):
    res = ''
    dictLen = len(dicts) - 1
    for i in range(leng):
        res += dicts[random.randint(0,dictLen)]
    return res

# 检查密码的等级
def checkPassword(passwd):
    res = ''
    if re.search(r'\d', passwd):
        res = 's'
        if re.search(r'[a-z]', passwd) and re.search(r'[A-Z]', passwd):
            res = 'c'
            if re.search(r'[_@!,.<>:;-=+/?]', passwd):
                res = 'd'
    return res

# 取得密码函数
def getPassword(leng,level,dicts):
    res = passwordMaker(leng, dicts)
    # 检查密码是否符合期望的条件，如果不负责，则重新生成一遍
    if checkPassword(res) != level:
        return getPassword(leng, level, dicts)
    return res

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

    # 设定三个等级的密码生成的词典
    sDict = '0123456789'
    cDict = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'
    dDict = cDict + '_@!,.:;-=+/?'
    # 根据命令行条件，打印最终的密码
    if args.simple:
        print(getPassword(length, 's', sDict))
    elif args.difficult:
        print(getPassword(length, 'd', dDict))
    else:
        # 默认输出为 一般复杂程度的密码
        print(getPassword(length, 'c', cDict))
