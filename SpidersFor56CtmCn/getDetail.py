#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests, markdown, os, time, json
from pyquery import PyQuery as pq
from tomd import Tomd
import jieba

def fullUrl (url):
    return 'http://news.chinawutong.com' + url

def osCmd (cmd):
    arr = os.popen(cmd).readlines()
    res = []
    for i in arr:
        res.append(i.encode('utf-8').decode('utf-8-sig').strip())
    return res

def url2str (url):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
            }
    r = requests.get(url, headers=headers)
    r.encoding = 'gb2312'
    return r.text

def getDate (text):
    timeStr = text.replace('更新时间：', '').split(' ')[0]
    try:
        time.strptime(timeStr, '%Y-%m-%d')
        return timeStr
    except err:
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def isChinese(word):
    for ch in word:
        if not '\u4e00' <= ch <= '\u9fff':
            return False
    return True

def getKeywords (text):
    arr = jieba.cut_for_search(text)
    res = []
    for i in arr:
        if isChinese(i):
            res.append(i)
    return ','.join(res)

def getArticle (url):
    text = url2str(url)
    hasUrl = len(osCmd('cat history.log | grep ' + url))
    if hasUrl == 0:
        os.system('echo ' + url + ' >> history.log')
        try:
            # 获取文章内容
            doc = pq(text)
            articleTitle = doc('.mainnews_l h1').text()
            articleDetails = doc('.mainnews_l .newsdetails')
            articleDate = getDate(doc('.mainnews_l .time').text())
            articleTime = str(int(time.time()))
            mdArticle = Tomd(str(articleDetails)\
                    .replace('&#13;','')\
                    .replace('\t','')\
                    ).markdown
            html = markdown.markdown(mdArticle)
            articleKey = getKeywords(articleTitle)
            if len(html) > 100:
                # 提交文章到系统
                curlCommand = "curl -s 'http://www.56.com/admin/index.php?controller=module&project=article&operate=save' -H 'Cookie: PHPSESSID=hm8kb0pg9l2cc9vgrve7als2r1' --data 'title={title}&classid=5&tags={key}&hits=0&info=&content={content}&time={time}&status=1&html=&template=%2Farticle_content.html&date={date}' --compressed".format(title=articleTitle, content=html, time=articleTime, date=articleDate, key=articleKey)
                res = json.loads(osCmd(curlCommand)[0])['status']
                if res == 'y':
                    print('文章添加成功' + url)
                else:
                    print('文章添加失败' + url)
            else:
                print('文章内容过短')
        except:
            print('文章抓取内容出错: ' + url)
    else:
        print('重复文章: ' + url)
    
def getList (url):
    doc = pq(url2str(url))
    listDom = doc('.newlist a')
    for i in listDom:
        getArticle(fullUrl(dict(i.attrib)['href']))

def getAll ():
    for i in range(1, 100):
        url = '/wlzx/wlrd/list_77_' + str(i) + '.html'
        getList(fullUrl(url))
if __name__ == '__main__':
    getAll()
    # testUrl = 'http://news.chinawutong.com/wlnxs/wlrgs/201908/58507.html'
    # getArticle(testUrl)
    # listUrl = '/wlzx/wlrd/list_77_1.html'
    # getList(fullUrl(listUrl))
    # print(getDate('更新时间：2019-09-05 11:50'))
