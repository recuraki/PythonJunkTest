#!/usr/local/bin/python
# -*- coding: utf-8 -*-

inSize = 20

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

for y, stTmp in enumerate(banner):
    cuMain.move(y, 0)
    cuMain.addstr("%s :%s" % stTmp)
cuMain.refresh()

cuSub = cuMain.subwin(inSize, inSize, len(banner) , 20)
# 左、右、上、下、左上、右上、左下、右下
cuSub.border("|", "|", "-", "-", "+", "+", "+", "+")

# 初期位置の決定
x = 1
y = 0
stDirection = "j"

# windowsのサイズを取得
max_y, max_x = cuSub.getmaxyx()
cuSub.refresh()
# getchのタイムアウトを設定
cuSub.timeout(100)

for i in range(1, inSize - 1):
    for j in range(1, inSize - 1):
        cuSub.addch(j, i, ".")

while True:
    inChar = cuSub.getch()
    if not inChar == -1:
        stChar = chr(inChar)
        if stChar == "k":
            stDirection = "k"
        if stChar == "j":
                stDirection = "j"
        if stChar == "h":
            stDirection = "h"
        if stChar == "l":
            stDirection = "l"
        if stChar == "q":
            os.exit()

    if stDirection == "k":
        y = y - 1
    if stDirection == "j":
        y = y + 1
    if stDirection == "h":
        x = x - 1
    if stDirection == "l":
        x = x + 1

    cuSub.move(y, x)

    cuSub.addstr("*")

time.sleep(1)
curses.nocbreak();
curses.echo()
curses.endwin()
