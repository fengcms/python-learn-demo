#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
# 获取文件类型库
import imghdr
# MD5库
import hashlib
# 文件操作库
import shutil
# 命令行分析库
import argparse

# 处理命令行参数，使用 argparse 库
parser = argparse.ArgumentParser()
# 定义脚本描述信息
parser.description='Move or copy the images in the source directory with the name of MD5 into the target directory'
# 定义脚本版本
parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')

# 添加源目录参数，必填
parser.add_argument('sourceDir', help='Select source directory')
# 添加目标目录参数，选填
parser.add_argument('targetDir', help='Select target directory', nargs='?')

# 定义一个互相排斥的参数，copy or move 不可同时存在
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", "--move", help="The way to operate the file is to move", action="store_true")
group.add_argument("-c", "--copy", help="The way to operate the file is to copy", action="store_true")

# 将参数命名为变量 args
args = parser.parse_args()

# 设定默认参数
sourceDir = args.sourceDir
targetDir = args.targetDir or args.sourceDir
operation = 'copy' if args.copy == True else 'move'
images = []

# 定义出错函数
def errUsage(res):
    print('error: ' + res)
    parser.print_usage()
    exit()

# 找到源目录下所有的图片
def findImage(sourceDir):
    # 如果源目录不存在，则报错退出
    if not os.path.exists(sourceDir):
        errUsage('Source directory is not defined')
    # 循环目标目录中的文件
    for fil in os.listdir(sourceDir):
        # 取得文件的路径
        filPath = os.path.join(sourceDir, fil)
        # 判断文件是否为目录
        if not os.path.isdir(filPath):
            # 判断文件是否为图片
            if imghdr.what(filPath) != None:
                # 将图片插入需要处理的列表
                images.append(filPath)
# 计算 MD5 值函数
def calcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

# 处理所有图片
def md5img(images):
    # 如果目标目录不存在，则报错退出
    if not os.path.exists(targetDir):
        errUsage('Target directory is not defined')

    method = {
        "move": shutil.move,
        "copy": shutil.copy
    }
    # 循环需要处理的图片列表
    for img in images:
        # 根据图片的真实后缀，来确定图片的后缀，如果是 jpeg 则改成 jpg
        postfix = 'jpg' if imghdr.what(img) == 'jpeg' else imghdr.what(img)
        # 执行复制或者移动操作
        method[operation](img, targetDir + '/' + calcMD5(img) + '.' + postfix)
# 找图片
findImage(sourceDir)
# 处理图片
md5img(images)
# 完成
print('Finish')
