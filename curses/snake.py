#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 盤面のサイズ(正方形)
inSize = 20
# 初期尻尾の長さ
MaxTail = 5
# ごはんの数
MaxFood = 3
inTime = 0

import time
import curses
import random 

# cursesの初期化
cuMain = curses.initscr()
# echoを抑制する
curses.noecho()
# enterを待たずにcursesで処理する
curses.cbreak()

banner = ( ("Dev", "kanai"), ("name", "snake"),)

# バナー表示のテスト
for y, stTmp in enumerate(banner):
    cuMain.move(y, 0)
    cuMain.addstr("%s :%s" % stTmp)

# 一旦、これで書く
cuMain.refresh()

# サブウィンドウの表示
cuSub = cuMain.subwin(inSize, inSize, len(banner) , 20)

# 左、右、上、下、左上、右上、左下、右下
cuSub.border("|", "|", "-", "-", "+", "+", "+", "+")

# 初期位置の決定
x = 1
y = 1
stDirection = "j"

# 情報の初期化
Tail = []
Food = []
isLive = True

# windowsのサイズを取得
max_y, max_x = cuSub.getmaxyx()
cuSub.refresh()
# getchのタイムアウトを設定
cuSub.timeout(100)

for i in range(1, inSize - 1):
    for j in range(1, inSize - 1):
        cuSub.addch(j, i, ".")

while isLive:

    # 一文字受け付ける
    inChar = cuSub.getch()

    # 文字コード"-1"はT/O = 入力がないのでスキップ
    if not inChar == -1:
        stChar = chr(inChar)
        # 移動は「向き」を変えるだけ
        if stChar == "k":
            stDirection = "k"
        if stChar == "j":
                stDirection = "j"
        if stChar == "h":
            stDirection = "h"
        if stChar == "l":
            stDirection = "l"
        if stChar == "q":
            isLive = False
            continue

    # 前の位置を"."で書き換える
    cuSub.move(y, x)
    cuSub.addstr(".")

    # 尻尾の位置を記録
    Tail = [(y, x)] + Tail

    # 移動する
    if stDirection == "k":
        y = y - 1
    if stDirection == "j":
        y = y + 1
    if stDirection == "h":
        x = x - 1
    if stDirection == "l":
        x = x + 1

    # 尻尾の最大長さを超えていたら短くする
    while len(Tail) > MaxTail:
        (ty, tx) = Tail[-1]
        cuSub.move(ty, tx)
        cuSub.addstr(".")
        # 最後尾[-1]をdelする
        del(Tail[-1])

    
    # 尻尾を描画
    for (ty, tx) in Tail:
        cuSub.move(ty, tx)
        cuSub.addstr("&")

    # Foodを描画
    for (ty, tx) in Food:
        cuSub.move(ty, tx)
        cuSub.addstr("%")

    # 当たり判定
    if x > (inSize - 1)  or x < 1:
        isLive = False
        continue
    if y > (inSize - 1) or y < 1:
        isLive = False
        continue
    if (y, x) in Tail:
        isLive = False
        continue

    # 現在位置を"*"で書き換える
    cuSub.move(y, x)
    cuSub.addstr("*")

    # Foodとの当たり判定
    if (y, x) in Food:
        Food.remove((y, x))
        MaxTail = MaxTail + 1

    inTime = inTime + 1

    # Foodをまく
    if True:
        if 0 < random.randint(0,100):
            need_plot = True
            if len(Food) > MaxFood + 1:
                need_plot = False
            while need_plot:
                cx, cy = random.randint(1,inSize - 2), random.randint(1,inSize - 2)
                if (cy, cx) in Tail:
                    continue
                if (cy, cx) in Food:
                    continue
                if (cy, cx) == (y, x):
                    continue
                Food = [(cy, cx)] + Food
                need_plot = False            

time.sleep(1)

curses.nocbreak();
curses.echo()
curses.endwin()
