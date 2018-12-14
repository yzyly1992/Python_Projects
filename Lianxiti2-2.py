#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:19:29 2018

@author: davidyang
"""

import random, string

class codeGenerator():
    
    def __init__(self, lens, nums):
        self.lens = lens
        self.nums = nums
        
    def generator(self):
        code = ''
        chars = string.ascii_letters + string.digits
        for i in range(self.lens):
            code = code + random.choice(chars).upper()
        print(code)
        
    def iters(self):
        for k in range(self.nums):
            self.generator()
            
appleCode = codeGenerator(10,10)
if __name__ == '__main__':
    appleCode.iters()