
def do():
    while True:
        from collections import deque
        w, h = map(int, input().split())
        if w == h == 0: break
        maze = []
        curh, curw = -1, -1
        maze.append("#" * (w+2))
        for hh in range(h):
            l = list("#" + input() + "#")
            if l.count("@"): curh, curw = hh + 1, l.index("@")
            maze.append(l)
        maze.append("#" * (w+2))
        maze[curh][curw] = "."
        q = deque([(curh, curw)])
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]
        ans = 0
        while len(q) > 0:
            curh, curw = q.popleft()
            if maze[curh][curw] == "#": continue
            maze[curh][curw] = "#"
            ans += 1
            for di in range(len(dh)):
                nexth, nextw = curh + dh[di], curw + dw[di]
                if maze[nexth][nextw] == "#": continue
                q.append( (nexth, nextw) )
        print(ans)

def do2():
    dh = [-1, 0, 0, 1]
    dw = [0, -1, 1, 0]
    while True:
        w, h = map(int, input().split())
        if w == h == 0: break
        maze = []
        curh, curw = -1, -1
        maze.append("#" * (w + 2))
        for hh in range(h):
            l = list("#" + input() + "#")
            if l.count("@"): curh, curw = hh + 1, l.index("@")
            maze.append(l)
        maze.append("#" * (w + 2))
        def search(h, w):
            if maze[h][w] == "#": return 0
            ans = 1
            maze[h][w] = "#"
            for di in range(len(dh)):
                ans += search(h + dh[di], w + dw[di])
            return ans
        print(search(curh, curw))


#do()
do2()