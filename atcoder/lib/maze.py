import sys
import math

def doTry(l, k, canfloor=2):
    # lの中で、連続するk個の"#"があるか？ただし、canfloor個までは"."が合っても良い O(N)
    l = list(l)
    if len(l) < k: return False
    cnt = 0
    for i in range(k):
        if l[i] == "#": cnt += 1
    if cnt >= (k - canfloor): return True
    for i in range(k, len(l)): # 今から読み込むindex
        if l[i] == "#": cnt += 1
        if l[i-k] == "#": cnt -= 1
        if cnt >= (k - canfloor): return True
    return False
print(doTry("######.", 6))
print(doTry("##..##.", 6))
print(doTry("##.###.", 6))

"""
 1  2  3  4
 5  6  7  8
 9 10 11 12
 があったとき、toLeftは
 [[1], [2, 5], [3, 6, 9], [4, 7, 10], [8, 11], [12]]
 を返す
"""
def diagonalListFromLeft(maze):
    ans = []
    hsize = len(maze)
    wsize = len(maze[0])
    for w in range(wsize):
        h = 0
        l = []
        while 0 <= w < wsize and 0 <= h < hsize:
            l.append(maze[h][w])
            h, w = h + 1, w - 1
        ans.append(l)
    for h in range(1, hsize):
        w = wsize - 1
        l = []
        while 0 <= w < wsize and 0 <= h < hsize:
            l.append(maze[h][w])
            h, w = h + 1, w - 1
        ans.append(l)
    return ans
maze = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(diagonalListFromLeft(maze)) # [[1], [2, 5], [3, 6, 9], [4, 7, 10], [8, 11], [12]]
maze = [[1,1,1,1,1,"#",1,1,1,1] for _ in range(10)]
print(maze)
print(diagonalListFromLeft(maze)) # [[1], [2, 5], [3, 6, 9], [4, 7, 10], [8, 11], [12]]

"""
 1  2  3  4
 5  6  7  8
 9 10 11 12
 があったとき、toRightは
 [[4], [3, 8], [2, 7, 12], [1, 6, 11], [5, 10], [9]]
 を返す
"""
def diagonalListFromRight(maze):
    ans = []
    hsize = len(maze)
    wsize = len(maze[0])
    for w in range(wsize-1, -1, -1):
        h = 0
        l = []
        while 0 <= w < wsize and 0 <= h < hsize:
            l.append(maze[h][w])
            h, w = h + 1, w + 1
        ans.append(l)
    for h in range(1, hsize):
        w = 0
        l = []
        while 0 <= w < wsize and 0 <= h < hsize:
            l.append(maze[h][w])
            h, w = h + 1, w + 1
        ans.append(l)
    return ans
maze = [[1,2,3,4], [5,6,7,8], [9,10,11,12]] # [[4], [3, 8], [2, 7, 12], [1, 6, 11], [5, 10], [9]]
print(diagonalListFromRight(maze))



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