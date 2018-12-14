#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 10:53:10 2018

@author: davidyang
"""

# -*- coding:utf-8 -*-
# 第0001题 作为Apple Store App 独立开发者，你要搞显示促销，为你的应用 生成激活码（或优惠券），使用Python如何生成200个激活码？#

import random, string

def random_str(num, length = 7):
    f = open('Running_result.txt', 'wb')
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choise(chars) for i in range(length)]
        f.write(''.join(s) + '\n')
    f.close()
    
if __name__ == '__main__':
    random_str(200)