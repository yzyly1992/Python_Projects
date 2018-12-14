#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:49:26 2018

@author: davidyang
"""

from PIL import Image, ImageFont, ImageDraw

image = Image.open('0.jpg')
w, h = image.size
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 120)
draw = ImageDraw.Draw(image)
draw.text((w-100, 10), '2', fill=(255, 10, 10), font=font)
image.save('1.jpg', 'JPEG')
