# https://note.nkmk.me/python-pillow-gif/
# https://note.nkmk.me/python-pillow-rotate/
from PIL import Image, ImageDraw
from copy import deepcopy
images = []
colorWhite = (255, 255, 255,0)

fn_arupaka = "./kawa.png"
fn_question = "./nc97468_ns.png"

size = 150

imArupaka = Image.open(fn_arupaka)
imArupaka = imArupaka.resize((100,100))
imQuestion = Image.open(fn_question)
imQuestion = imQuestion.resize((40,40))

im = Image.new('RGBA', (size, size), colorWhite)

rot = 30
step = 10
pertime = 20*step
angles = []
for i in range(0, -abs(rot), -step):
    angles.append(i)
for i in range(-abs(rot), abs(rot), step):
    angles.append(i)
for i in range(abs(rot), 0,-step):
    angles.append(i)
qs = []
qs.append((5,25))
qs.append((50,5))
qs.append((100,25))
for i in angles:
    im = Image.new('RGBA', (size, size), colorWhite)
    imQuestionNew = imQuestion.rotate(i, resample=Image.BICUBIC)
    im.paste(imArupaka, (30, 50))
    for pos in qs:
        im.paste(imQuestionNew, pos, imQuestionNew)
    images.append(deepcopy(im))

print(len(images))

images[0].save('a.gif', save_all=True, append_images=images[1:], optimize=False, duration=pertime, loop=0)