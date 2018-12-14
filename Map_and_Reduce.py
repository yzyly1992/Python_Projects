#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:19:22 2018

@author: davidyang
"""
# test 1
#maxx = {'a': 'A', 'b': 'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N','o':'O','p':'P', 'q':'Q', 'r':'R','s':'S', 't':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
#minn = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','G':'g','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
#def normalize(L):
#    if L[0] in maxx:
#        return L[0] == maxx[L[0]]
#        
#    for n in L[1:len(L)]:
#        if n in minn:
#            return L[n] == minn[n]
#    return L
#
#def nnnn(L):
#    return map(normalize, L)

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# test 2
from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)
    
print(prod([3, 5, 7, 9]))

#test 3
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    int_part, dec_part = s.split('.')
    return reduce(lambda x, y: 10*x + y, map(int, int_part)) + \
        reduce(lambda x, y: 10*x + y, map(int,dec_part))*10**(-len(dec_part))

print(str2float('123.456'))        
