#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse

a = []
def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def calc(num):
    for i in range(2,int(num**0.5) + 1):
        if num%i == 0:
            a.append(i)
            if isPrime(num/i):
                a.append(int(num/i))
            else:
                calc(num/i)
            break
def echo(a):
    res = '该数字的质因数结果是：'
    for i in a:
        res += str(i) + '*'
    print(res[0:len(res) - 1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type=int, help='请输入要计算质因数的数字')
    args = parser.parse_args()
    calc(args.num)
    if len(a) == 0:
        print('该数为质数')
    else:
        echo(a)
        print('该数字的质因数结果是：' + str(a)[1:len(str(a)) - 1].replace(', ','*'))
