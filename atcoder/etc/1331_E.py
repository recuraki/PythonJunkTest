from PIL.PIL import Image
im = Image.open("1331_E.png")

#RGBに変換
rgb_im = im.convert('RGB')

#画像サイズを取得
size = rgb_im.size

#取得したサイズと同じ空のイメージを新規に作成
im2 = Image.new('RGBA',size)

#loop
#x
for x in range(7, size[0], 15):
    #y
    for y in range(7, size[1], 15):
        #ピクセルを取得
        r,g,b = rgb_im.getpixel((x,y))
        #print(r,g,b)
        if g < 200:
            print("({0}, {1}),".format(x//15,y//15))

