#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import  urllib.request
from bs4 import BeautifulSoup
import os


def getid (x):
    url = r'https://blog.csdn.net/fungleo/article/list/'+str(x)
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('div', 'article-item-box')

    for i in links:
        idStr = i['data-articleid']
        timeStr = i.find_all('span', 'date')[0].string
        outStr = '("' + idStr + '", "' + timeStr + '"),\n'
        with open('idtime.txt', 'a+') as f:
            f.write(outStr)
            f.close()
        # iHtml = BeautifulSoup(str(i),'html.parser')
        # os.system('echo ' + str(i.a['href']).replace('https://blog.csdn.net/fungleo/article/details/', '') + ' >> id.txt')
        # print(i.a['href'])

def do ():
    for i in range(14):
        getid(i)
        
#getid(1)
do()
