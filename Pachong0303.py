#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:20:37 2018

@author: davidyang
"""

#coding:utf-8
# BeatifulSoup抓取
import urllib #python3中urllib整合了五大模块urllib.error, urllib.parse, urllib.response, urllib.robotparser
import re
from bs4 import BeautifulSoup
print("=============获取网页源代码============")
host = 'http://news.sina.com.cn/'
text = urllib.request.urlopen(host).read()

print("=============解析网页源代码============")
soup = BeautifulSoup(text, 'html.parser') #前一个参数为要解析的文本，后一个参数为解析模型
# bs4 的html解析器： BeatufulSoup(mk, 'html.parser')
# lxml的html的解析器： BeautifulSoup(mk, 'lxml')--pip install lxml
# lxml 的xml解析器： (mk, 'xml')
# html5lib的解析器 （mk, 'html5lib')
# print(soup.prettify()) #打印解析内容

print("============对象划分==============")
# 解析后全部html代码转化为四中类型：
# 基本对象类型
# 1， Tag---标签，最基本的信息组织单元，分别用<>和</>表明开头和结尾
# 1.1  标签Nam属性--标签的名字， <p>...</p> 的名字是'p', 格式：<tag>.name
# 1.2 标签attributes属性标签的属性， 格式：<tag>.attrs
#......

#print(soup.a)
#print(soup.a.string)
#print(type(soup.a.string))
#
#print(soup.title)
#print(soup.head)
#
#print("=============获取标签内容属性=============")
#for tag in soup('a'):
#    link = tag.attrs['href']
#    link = tag['href']
#    link = tag.get('href')
#    print(tag.get_text())
#    print(urllib.parse.urljoin(host,link))
#    print(tag.name),
#    print(tag.attrs),
#    print(tag.string)
#    
#print("==========搜索============")
#print("==========搜索-按标签搜索===========")
#print(soup.find_all('a', limit = 10)) #按字符串查询
#print(soup.find_all(re.compile("^a"))[3]) #按正则式查询
#print(soup.find_all(["a", "b"])[4]) #安列表查询
#print(soup.find_all(True)[1]) #查询所有元素，第一个袁术是heml元素，就是整个全文
#
#print("==========搜索-按文本收缩============")
#print(soup.find_all(text = "军事"))
#print(soup.find_all("a", limit = 2, recursive = False))
#
#print("============暗属性搜索============")
#print(soup.find_all(id='headerImg')) #按属性值查询
print(soup.find_all(href=re.compile("finance")))  #按属性值得正则表达式查询
#print(soup.find_all(href= re.compile(".*index\.html"), target= '_blank')) #按属性值列表查询
