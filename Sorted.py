#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:55:52 2018

@author: davidyang
"""

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = lambda x : x[1])
print(L2)

