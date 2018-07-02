#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import linecache
import requests as req
from io import BytesIO
import json
import os
import time

imgDict = './imgOldUrlBak.txt'

#print(Cookie)

with open(imgDict, 'r', encoding="utf-8") as imgDictTxt:
    for lin in imgDictTxt:
        if 'csdn' in lin:
            imgUrl = lin
            imgReq = req.get(imgUrl, headers=headers, cookies=cookies)
            img = BytesIO(imgReq.content)
            if imgReq.status_code == 200:
                files = {'file': ('imgName', img, 'image/jpeg')}
                r = req.post('http://localhost:7000/upimg', files=files)
                rJson = json.loads(r.text)
                if rJson['status'] == 0:
                    rPath = rJson['data']['path']
                    os.system('echo "' + imgUrl + '\t' + rPath + '" >> imgDict.txt')
                    print('Succ: ' + rPath)
                else:
                    os.system('echo "' + imgUrl + '" >> imgErr.txt')
                    print('upErr: ' + imgUrl)
            else:
                time.sleep(0.1)
                print(imgReq.status_code)
                print('downErr: ' + imgUrl)


