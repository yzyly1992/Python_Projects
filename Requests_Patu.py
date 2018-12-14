#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:54:23 2018

@author: davidyang
"""

import requests
from bs4 import BeautifulSoup
import os
import re
#获取html
chromeHeader = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
f = requests.get(url = 'https://www.zhainanfulishe.net/tag/%E9%82%AA%E6%81%B6gif%E5%87%BA%E5%A4%84', headers = chromeHeader).text
#用BS解析html
s = BeautifulSoup(f, 'lxml')
s_imgs = s.find_all('img', limit = 10)
#逐个将图片保存到本地
i = 1
for s_img in s_imgs:
    img_url = s_img['src']
    if re.match(r'.*\.gif', img_url):
        img_content = requests.get(url = img_url, headers = chromeHeader).content
        file_name = str(i) + 'Good.gif'
        with open(os.getcwd() + '/' + file_name, 'wb') as wf:
            wf.write(img_content)
    i += 1
