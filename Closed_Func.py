#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:48:19 2018

@author: davidyang
"""

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter


def createCounter2():
    n = [0]
    def counter():
        n[0] += 1
        return n[0]
    return counter


f1, f2, f3 = createCounter()

