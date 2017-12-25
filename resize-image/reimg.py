#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse
import os
import imghdr
from PIL import Image

# 错误退出函数
def errMsn(msn):
    print('\033[31mError:\033[0m ' + msn)
    parser.print_usage()
    exit()

# 在源目录中找到所有图片并输出为数组
def findImg(sdir):
    res = []
    if not os.path.exists(sDir):
        errMsn('Source directory don\'t exist')
    for f in os.listdir(sdir):
        fp = os.path.join(sdir, f)
        if not os.path.isdir(fp):
            if imghdr.what(fp):
                res.append(fp)
    if len(res) == 0:
        errMsn('There is no image in the source directory')
    else:
        return res

# 循环缩放所有图片
def resizeImg(arr, size, tdir, imgQual):
    for img in arr:
        simg = Image.open(img)
        simg_w = simg.size[0]
        simg_h = simg.size[1]
        
        # 如果原图片宽高均小于设置尺寸，则将原图直接复制到目标目录中
        if simg_w <= size and simg_h <= size:
            simg.save(tdir + '/' + os.path.basename(img), quality=imgQual)
        else:
            # 比较源图片的宽高，计算处理后的宽高
            timg_w = size
            timg_h = int(size * simg_h / simg_w)
            if simg_w < simg_h:
                timg_w = int(size * simg_w / simg_h)
                timg_h = size
            # 缩小图片并保存
            timg = simg.resize((timg_w, timg_h),Image.ANTIALIAS)
            timg.save(tdir + '/' + os.path.basename(img), quality=imgQual)
    print('\033[32mSuccess:\033[0m Task Finish')

# 目标目录处理函数
def checkTargetDir(sdir, tdir):
    # 如果目标目录为空时提示用户确认
    if not tdir:
        print('\033[33mWarning:\033[0m If the target directory isn\'t set, the processing '\
                'results will cover the picture in the source directory\n'\
                '\033[36mWhether to Continue(Y/n)\033[0m ')
        confirm = input('Confirm:')
        if confirm in ('', 'Y', 'y'):
            print('\033[34mInfo:\033[0m The target directory is ' + sdir)
            return sdir
        else:
            exit()
    else:
        # 如果目标目录设定，但是不存在，则提示用户是否创建目标目录
        if not os.path.exists(tdir):
            print('Target directory don\'t exist\n'\
                    '\033[36mWhether to create the Target directory(Y/n)\033[0m')
            confirm = input('Confirm:')
            if confirm in ('', 'Y', 'y'):
                os.makedirs(tdir)
                return tdir
            else:
                exit()
        else:
            return tdir

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.description='Reduce the picture in the source directory and save it to \
            the target directory based on the longest side parameters'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    parser.add_argument('size', type=int, help='The max width or max height of a picture')
    parser.add_argument('sourceDir', help='Source directory')
    parser.add_argument('targetDir', help='Target directory', nargs='?')
    parser.add_argument('-q', '--quality', type=int, help='Save picture quality, default 60')
    args = parser.parse_args()

    size = args.size
    sDir = args.sourceDir
    tDir = checkTargetDir(sDir,args.targetDir)
    imgQual = args.quality or 60
    # 执行处理 
    resizeImg(findImg(sDir), size, tDir, imgQual)
