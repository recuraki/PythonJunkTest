# -*- coding:utf-8 -*-
from PIL import Image

# 透過したい画像を読み込み
org = Image.open('nc97468.png')
# 同じサイズの画像を作成
trans = Image.new('RGBA', org.size, (0, 0, 0, 0))
width = org.size[0]
height = org.size[1]
for x in range(width):
    for y in range(height):
        pixel = org.getpixel((x, y))

        # 白なら処理しない
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            continue

        # 白以外なら、用意した画像にピクセルを書き込み
        trans.putpixel((x, y), pixel)
# 透過画像を保存
trans.save('nc97468_ns.png')
