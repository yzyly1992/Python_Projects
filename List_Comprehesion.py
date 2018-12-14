#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:58:56 2018

@author: davidyang
"""

L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = []
#[L2.append(s.lower()) for s in L1 if isinstance(s, str)==True]
#print(L2)

L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

l = [1]
while l:
    yield l
    l = [1] + [ l[n] + l[n+1] for n in range(len(l) - 1) + [1]]