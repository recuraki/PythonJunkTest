from PIL import Image, ImageDraw, ImageChops, ImageEnhance
from copy import deepcopy
oimg = Image.open("animal_arupaka.png")
oimg = oimg.resize((oimg.width // 2, oimg.height // 2))
img = deepcopy(oimg)
dat = img.split()
r,b,g,a = img.split()

basecolor = (212, 195, 188) #毛の色
cangap = 20
# 毛を推察する。+-gapは許容
r = r.point(lambda x: 1 if basecolor[0] - cangap <= x <= basecolor[0] + cangap else 0, mode="1")
g = g.point(lambda x: 1 if basecolor[1] - cangap <= x <= basecolor[1] + cangap else 0, mode="1")
b = b.point(lambda x: 1 if basecolor[2] - cangap <= x <= basecolor[2] + cangap else 0, mode="1")

img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

ph = 0
dankai = 7

animationgif = []
colors = []
colors.append((0xff, 0x45, 0x00))
colors.append((0xff, 0x8c, 0x00))
colors.append((0xff, 0xff, 0x00))
colors.append((0x22, 0x8b, 0x22))
colors.append((0x41, 0x69, 0xe1))
colors.append((0x19, 0x19, 0x70))
colors.append((0xc7, 0x15, 0x85))

for loop in range(dankai):
    img = oimg.copy()
    for i in range(dankai):
        # アルパカの毛皮
        mask = ImageChops.logical_and(r, g)
        mask = ImageChops.logical_and(mask, b)
        d = ImageDraw.Draw(mask) # 毛皮塗る

        newh = int(mask.height / dankai * i) + int(mask.height / dankai * loop) # 新しく塗る高さ
        newh += 3
        newh = newh % mask.height
        haba = mask.height // dankai + 2 # 塗る幅
        d.rectangle([(0,0), (mask.width, newh)], fill="black") #その区間より上を黒でマスク
        d.rectangle([(0, newh+ haba), (mask.width, mask.height)], fill="black") # 同じく下をマスク
        # ペンキのように塗る
        dst_color = (int(128-128/dankai*i),int(128/dankai*i),int(64+192//dankai*i))
        dst_color = colors[i]
        img.paste(Image.new("RGBA", img.size, dst_color), mask=mask)
        amask = Image.eval(a, lambda x: 255 if x < 128 else 0)
        img.paste(0, mask=amask)
        ph = newh
    animationgif.append(img)

print(animationgif)
animationgif[0].save('chaki.gif',
               save_all=True, append_images=animationgif[1:], optimize=False, duration=100, loop=0)
