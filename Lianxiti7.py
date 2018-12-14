#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:02:28 2018

@author: davidyang
"""

import os

files = os.listdir('/Users/davidyang/Documents/Coding/Python')

eLines = 0
aLines = 0
tLines = 0

for file in files:
    if file.split('.')[-1] == 'py':
        f = open(file).readlines()
        for mf in f:
            if mf[0] == '#':
                aLines += 1
            elif mf.strip() == '':
                eLines += 1
        tLines += len(f)
fLines = tLines - eLines - aLines

print('写了%d代码\n' % fLines)
print('写了%d注释\n' % aLines)
print('写了%d空行' % eLines)


    
            