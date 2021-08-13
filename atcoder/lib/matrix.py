

# 左に回す
"""
12
45
78
258
147"""
maze = ["12", "45", "78"]
for s in maze:print(s)
h, w = len(maze), len(maze[0])
newmaze = []
for ww in range(w):
    s=""
    for hh in range(h):
        s += maze[hh][w-ww-1]
    newmaze.append(s)
h, w = w, h
maze = newmaze
for s in maze:print(s)
