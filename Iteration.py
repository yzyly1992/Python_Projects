#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:32:20 2018

@author: davidyang
"""

def findMinAndMax(L):
    min = None
    max = None
    if L == []:
        return min, max
    else:
        min = max = L[0]
        for i in L:
            if i > max:
                max = i
            elif i < min:
                min = i
        return min, max
        
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
        
        