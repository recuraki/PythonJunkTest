import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    movedelta =  ((0, -1), (-1, 0), (1,0), (0,1))
    def do():
        from collections import deque
        hh, ww, percost = map(int, input().split())
        maze = []
        for _ in range(hh):
            dat = list(map(int, input().split()))
            maze.append(dat)
        visited = [[False] * ww for _ in range(hh)]
        q = deque([]) # h, w, cost
        q.append((0,0,0))
        visited[0][0] = True
        # BFS
        directcost = 10**18
        portalsh, portalsw, potralscost = -1, -1, 10**18
        portalth, portaltw, potraltcost = -1, -1, 10**18
        if maze[0][0] > 0 :
            potralscost = maze[0][0]
        while len(q) > 0:
            curh, curw, curcost = q.popleft()
            if curh == hh-1 and curw == ww-1:
                directcost = curcost
            #print(curh, curw)
            for dh, dw in movedelta:
                nh, nw = curh + dh, curw + dw
                if not (0 <= nh < hh):
                    continue
                if not (0 <= nw < ww):
                    continue
                if visited[nh][nw]:
                    continue
                if maze[nh][nw] == -1:
                    continue
                visited[nh][nw] = True
                q.append( (nh, nw, curcost + percost) )
                if maze[nh][nw] != 0:
                    newpcost = curcost + percost + maze[nh][nw]
                    if newpcost < potralscost:
                        potralscost = newpcost
                        #print("newportal", potralscost)

        visited = [[False] * ww for _ in range(hh)]
        q = deque([]) # h, w, cost
        q.append((hh-1, ww-1,0))
        visited[hh-1][ww-1] = True
        if maze[hh-1][ww-1] > 0 :
            potraltcost = maze[hh-1][ww-1]
        while len(q) > 0:
            curh, curw, curcost = q.popleft()
            for dh, dw in movedelta:
                nh, nw = curh + dh, curw + dw
                if not (0 <= nh < hh):
                    continue
                if not (0 <= nw < ww):
                    continue
                if visited[nh][nw]:
                    continue
                if maze[nh][nw] == -1:
                    continue
                visited[nh][nw] = True
                q.append( (nh, nw, curcost + percost) )
                if maze[nh][nw] != 0:
                    newpcost = curcost + percost + maze[nh][nw]
                    if newpcost < potraltcost:
                        potraltcost = newpcost
                        #print("newportal", potraltcost)

        res = min(directcost, potralscost + potraltcost)
        if res == 10**18:
            print(-1)
        else:
            print(res)


    do()







class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """10 6 2
0 0 0 1 0 0
-1 -1 0 0 0 -1
9 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 3"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()