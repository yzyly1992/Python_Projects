#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:18:55 2018

@author: davidyang
"""

import requests

response = requests.get(url = "http://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))

response.encoding = "utf-8"
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))