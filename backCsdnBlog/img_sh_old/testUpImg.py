#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import linecache
import requests as req
from io import BytesIO
import json
import os
import time


imgUrl = 'https://www.mediaatelier.com/CheatSheet/imgs/main.png'
imgReq = req.get(imgUrl)
print(imgReq)
#print(dir(imgReq))

