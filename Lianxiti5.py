#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:40:18 2018

@author: davidyang
"""

import os
from PIL import Image

ext = ['jpg', 'jpeg', 'png']
files = os.listdir('/Users/davidyang/Documents/Coding/Python')

#def process_image(filename, mwidth = 640, mheight = 1136):
#    image = Image.open(filename)
#    w, h = image.size
#    if w <= mwidth and h <= mheight:
#        print(filename, 'is OK')
#        return
#    if 1.0 * w / mwidth > 1.0 * h / mheight:
#        scale = 1.0 * w / mwidth
#        new_im = image.resize((int(w/scale), int(h/scale)),Image.ANTIALIAS)
#    else:
#        scale = 1.0*h/mheight
#        new_im = image.resize((int(w/scale),int(h/scale)), Image.ANTIALIAS)
#    new_im.save('new-' + filename)
#    new_im.close()
#    
#    
#for f in files:
#    if f.split('.')[-1] in ext:
#        process_image(f)
        
def process_image(filename, mwidth = 640, mheight = 1136):
    image = Image.open(filename)
    w, h = image.size
    if w > mwidth or h >mheight:
        scale = max(1.0 * w/mwidth, 1.0 * h/mheight)
        new_im = image.resize((int(w/scale), int(h/scale)),Image.ANTIALIAS)
        new_im.save('new-' + filename)
        new_im.close()
    
for file in files:
    if file.split('.')[-1] in ext:
        process_image(file)
