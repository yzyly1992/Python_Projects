#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:18:44 2018

@author: davidyang
"""
#import string
#
#f = "i? AM  am   !good "
#rf = f.translate(str.maketrans("","",string.punctuation))
#tf = rf.lower().split()
#collection = {}
#for item in tf:
#    collection[item] = item.count(item)
#print(collection)

#def word_count(string):
#  my_string = string.lower().split()
#  my_dict = {}
#  for item in my_string:
#    my_dict[item] = item.count(item)
#  print(my_dict)
#
#word_count("I am, that! I am")

import string
import codecs
import operator

class countWords():
    
    def __init__(self, path,rankNum):
        self.path = path
        self.rankNum = rankNum
    def count(self):
        wordSet = {}
        f = codecs.open(self.path, 'r',encoding = 'utf-8', errors = 'ignore')
        tf = f.read().translate(str.maketrans('','',string.punctuation))
        rf = tf.lower().split()
        for i in rf:
            if i in wordSet:
                wordSet[i] += 1
            else:
                wordSet[i] = 1
        return wordSet
        
    def rank(self):
        wordSet = self.count()
        rankSet = sorted(wordSet.items(), key = operator.itemgetter(1), reverse=True)
        print(rankSet[:self.rankNum])
        
k = countWords('novel.txt',4)
if __name__ == '__main__':
    k.rank()