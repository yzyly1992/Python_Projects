#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:54:50 2018

@author: davidyang
"""

def trim(s):
    while s[:1] == ' ':
        s = s[2:]
    while s[-1:] ==' ':
        s = s[:-2]
    return s

#def trim(s):
# 使用 while True: 可以一直循环：直到用 break 停止
#    while True:
#        if s == '':
#            break
#        elif s[0] == ' ':
#            s = s[1:]
#        elif s[-1] == " ":
#            s = s[:-1]
#        else:
#            break
#    return s
    
# s[0]==' '会错，这个是因为是s[0]超出了索引范围，会报错，而超出切片范围会返回空，而不会报错。

#def trim(s):
#    while True:
#        if s[:1] == ' ':
#            s = s[1:]
#        elif s[-1:] == " ":
#            s = s[:-1]
#        else:
#            break
#    return s

    
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')