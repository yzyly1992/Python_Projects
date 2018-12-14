#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:09:18 2018

@author: davidyang
"""

f = open('Running_result.txt','r')
judge = 0
mf = f.read().split('\n')
inp = input('please enter the key words!')
for i in mf:
    if i in inp:
        inp = inp.replace(i,len(i)*'*')

print(inp)
        
#if judge == 0:
#    print('H')
    

        

