#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import argparse
import os
import time
import clipboard
import db

# 根据需要的结果，剪出一个数组
def cutLength(leng, level):
    # 算法比较复杂，简化来说，就是已知数组长度，和数组内数字的和
    # 求一个随机的数组，满足上面的两个条件
    res = []
    for i in range(level, 1, -1):
        res.append(random.randint(1, leng - sum(res) - i + 1))
    res.append(leng - sum(res))
    # 因为第一位生成大数字的几率高于后面的几位，
    # 所以在得到结果后，随机排序一下,以期待更随机一些
    random.shuffle(res)
    return res
# 根据上面生成的数组和对应的字典，制造一个密码数组
def makePassword(dists, arr):
    res = []
    # 根据字典和数组，循环生成密码
    for i in range(len(arr)):
        # res += random.choices(dists[i], k=arr[i])
        for j in range(arr[i]):
            res += random.choice(dists[i])
    # 得到结果后，再一次随机排序
    random.shuffle(res)
    # 最后把数组变成字符串，并输出
    return ''.join(res)
# 生成一个密码函数
def getPassword(leng, level):
    # 根据密码长度和等级，去求一个满足条件的数组
    arr = cutLength(leng,level)
    # 制造字典
    str1 = '01'
    str2 = '23456789'
    str3 = 'abcdefghijkmnpqrstuvwxyz'
    str4 = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    str5 = '_@!,.:;-=+/?'

    dists = {
                1: [str1 + str2],
                3: [str2, str3, str4],
                4: [str2, str3, str4, str5]
            }
    # 生成密码
    return makePassword(dists[level], arr)

# 输出结果
def returnPassword(passwd, name):
    clipboard.copy(passwd)
    print('New password:\t\033[31m' + passwd + '\033[0m\nTip: The password has been copied to the clipboard')
    if name:
        print('And the password has been saved in data base')
    exit()

# 主函数
if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.description='This program is used to generate simple or complex passwords'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    parser.add_argument('length', type=int, help='The length of the password (Default 8)', nargs='?')
    parser.add_argument('-n', '--name', help='Take a name for your password and Write it in  data base')

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
    
    # 默认密码等级为一般
    level = 3

    if args.simple:
        level = 1
    if args.difficult:
        level = 4
    
    # 去得到密码
    res = getPassword(length, level)
    # 如果密码需要保存，则写入文件
    if args.name:
        db.insertDb(args.name,res)
        #writePassword(args.name, res)
    # 返回结果
    returnPassword(res, args.name)
