
import cv2
import numpy
import math

img = cv2.imread("maze3.PNG", cv2.IMREAD_GRAYSCALE)

boader = 128
cellsize = 5
judgenum = math.floor(cellsize * cellsize / 10)

height = img.shape[0]
width = img.shape[1]
print("{0} x {1}".format(height, width))
"""
# 白黒にする
for x in range(width  ):
    for y in range(height):
        if img[y,x] < boader:
            img[y,x] = 0
        else:
            img[y,x] = 255

cv2.imshow('image', img)
cv2.waitKey(0)
"""

# ブロック化
dat = list()
for y in range(math.floor(height / cellsize) - 1):
    line = list()
    for x in range(math.floor(width / cellsize) - 1):
        counter = 0
        for x2 in range(x * cellsize, (x + 1) * cellsize):
            for y2 in range(y * cellsize, (y + 1) * cellsize):
                if img[y2, x2] < boader:
                    counter = counter + 1
        if counter > judgenum:
            line.append(1)
            for x2 in range(x * cellsize, (x + 1) * cellsize):
                for y2 in range(y * cellsize, (y + 1) * cellsize):
                    img[y2, x2] = 0
        else:
            line.append(None)
            for x2 in range(x * cellsize, (x + 1) * cellsize):
                for y2 in range(y * cellsize, (y + 1) * cellsize):
                    img[y2, x2] = 255
    dat.append(line)

s = str(dat)

print(s.replace("None", "null"))



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()