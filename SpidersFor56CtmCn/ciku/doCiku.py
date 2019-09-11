#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
res = {}
def isChinese(word):
    for ch in word:
        if not '\u4e00' <= ch <= '\u9fff':
            return False
    return True

with open('./ciku.txt','r') as f:
    for line in f:
        arr = line.strip().split(',')
        if len(arr) == 2:
            k = arr[0]
            v = arr[1]
            if len(k) >= 2 and isChinese(k) and isChinese(v):
                if k not in res:
                    res[k] = []
                if len(v) >= 2:
                    res[k].append(v)

arr = []
for i in res:
    res[i] = list(set(res[i]))
    if len(res[i]) == 0:
        arr.append(i)

for i in arr:
    res.pop(i)

data = json.dumps(res)
with open('ciku.json','w') as f:
    f.write(data)
