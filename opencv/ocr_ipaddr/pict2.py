# thx:
# https://qiita.com/shinya187/items/f9a70fd52cc91ddb4ed7
# https://blog.machine-powers.net/2018/08/04/pyocr-and-tips/

# Windows Tesseract
# https://github.com/UB-Mannheim/tesseract/wiki
# add  "c:\Program Files\Tesseract-OCR" to path

"""
request
 opencv-python
 pyocr
"""

import cv2
import pyocr
import sys
from PIL import Image
import dns.resolver
import re
import os

fn = "./pict2.jpg"
im = cv2.imread(fn)
sizey, sizex, _ = im.shape
print("size x,y : {0} x {1}".format(sizex, sizey))

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.GaussianBlur(im, (9,9), 0)

im = cv2.adaptiveThreshold(
    im, 255
    , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY
    , 31 , 1)


#im = cv2.bitwise_not(im)


im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
cv2.imwrite("pict2_out.jpg",im_rgb)
im_txt = Image.open("pict2_out.jpg")

# ocr prep
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

# べたーっと文字で吐く
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = tool.image_to_string(im_txt,lang="eng")
print(txt)


# sys.exit(0)
cv2.imshow("debug", im)
cv2.waitKey(0)