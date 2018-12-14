#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 08:43:18 2018

@author: davidyang
"""
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

def get_one_page(url, chromeHeader):
    try:
        response = requests.get(url = url, headers = chromeHeader)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*board-img.*?src="(.*?)"></a>.*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        return {'index': item[0],'image': item[1],'title': item[2],'actor': item[3].strip()[3:],'time': item[4].strip()[5:],'score': item[5] + item[6]}
        
def write_to_file(content):
    with open('MovieResult.txt', 'a', encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii = False) + '\n')
        f.close()
        
def main(offset):
    chromeHeader = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url, chromeHeader)
    for item in parse_one_page(html):
        write_to_file(item)
    
if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])