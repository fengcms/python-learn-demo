#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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

def checkInput():
    num = input('输入: ')
    while not num.isdigit():
        print('输入的内容必须是正整数哦！')
        num = input('输入: ')
    return int(num)

def echo(num, a):
    res = '数字'+str(num)+' 的质因数结果是: '
    if len(a) == 0:
        res += str(num)
    else:
        res += str(a)[1:len(str(a))-1].replace(', ','*')
    return res

if __name__ == '__main__':

    print('这是一个计算一个数字的质因数的程序\n请输入您要计算质因数的数字')
    
    num = checkInput()
    a = []
    calc(num)
    print(echo(num, a))
