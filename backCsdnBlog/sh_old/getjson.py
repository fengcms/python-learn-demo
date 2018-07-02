#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import json
import os
r = requests.get('https://cnodejs.org/api/v1/topic/5433d5e4e737cbe96dcef312')
#print(dir(r))
os.system('echo ' + json.dumps(r.text) + ' > test.json')
#print(json.dumps(str(r.content)))
print(type(r.text))
