# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:24:55 2020

@author: Administrator
"""


import tesserocr as ocr
from PIL import Image

# image  = Image.open('code2.jpg')

# result = ocr.image_to_text(image)

# text = ocr.file_to_text('code2.jpg')

# #灰度化
# image = Image.open('code.jpg')
# image = image.convert('L')
# result = ocr.image_to_text(image)


#二值化
# image_bin = image.convert('1')
# image.show()


#灰度化以后再二值化
image1 = Image.open('code.jpg')
image = image1.convert('L')
thred = 125
table = []
for i in range(256):
    if i<thred:
        table.append(0)
    else:
        table.append(i)

image = image.point(table, '1')
image.show()

a = ocr.image_to_text(image)
