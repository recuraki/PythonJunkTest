import sys
import math

#ある地点をクリックした時、隣接のそれを塗りつぶす
def maze_fill():
    th, tw = [int(i) for i in input().split()]
    new_color = int(input())
    h, w = [int(i) for i in input().split()]
    maze = []
    for i in range(h):
        l = map(int ,input().split())
        l = list(l)
        maze.append(l)
    #for i in range(h):
    #    print(" ".join(list(map(str, maze[i]))))

    fcolor = maze[th][tw]
    dw = [0, 1, 0, -1]
    dh = [-1, 0, 1, 0]
    import collections
    q = collections.deque([])
    q.append([th, tw])
    while len(q) > 0:
        curh, curw = q.popleft()
        maze[curh][curw] = new_color
        for d in range(len(dw)):
            nh = curh + dh[d]
            nw = curw + dw[d]
            if nh < 0 or nw < 0:
                continue
            if (h-1) < nh or (w-1) < nw:
                continue
            if maze[nh][nw] == fcolor:
                q.appendleft([nh, nw])
    for i in range(h):
        print(" ".join(list(map(str, maze[i]))))

def ABC177D():
    def do():
        h, w = map(int, input().split())
        sh, sw = map(int, input().split())
        gh, gw = map(int, input().split())
        sh -= 1
        sw -= 1
        gh -= 1
        gw -= 1
        maze = []
        for _ in range(h):
            l = list(input())
            maze.append(l)

        dh = [-1, 0, 1, 0]
        dw = [0, 1, 0, -1]
        import collections
        q = collections.deque([])
        q.append([sh, sw, 0])
        res = -1
        while len(q) > 0:
            curh, curw, curcnt = q.popleft()
            if curh == gh and curw == gw:
                res = curcnt
                break
            if maze[curh][curw] == "#":
                continue
            maze[curh][curw] = "#"
            for d in range(len(dh)):
                nh, nw = curh + dh[d], curw + dw[d]
                if 0 <= nh and nh <= h - 1 and 0 <= nw and nw <= w - 1:
                    if maze[nh][nw] != "#":
                        q.appendleft([nh, nw, curcnt])
            for deltah in range(-2, 3):
                for deltaw in range(-2, 3):
                    nh, nw = curh + deltah, curw + deltaw
                    if 0 <= nh and nh <= h - 1 and 0 <= nw and nw <= w - 1:
                        if maze[nh][nw] != "#":
                            q.append([nh, nw, curcnt + 1])