import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63

    def do():
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]

        INF = -100
        oh, ow = map(int, input().split())
        maze = []
        visited = []
        # INF:壊せない壁, 0:通路 -1:壁
        l = [INF] * (ow + 2)
        maze.append(l)
        l = [-1] * (ow + 2)
        visited.append(l)

        for _ in range(oh):
            s = input()
            l = [INF]
            for x in s: l.append(0 if x=="." else -1)
            l.append(INF)
            maze.append(l)
            l = [-1] * (ow + 2)
            visited.append(l)

        l = [INF] * (ow + 2)
        maze.append(l)
        l = [-1] * (ow + 2)
        visited.append(l)


        from collections import deque
        q = []
        # kaisuu, h, w
        q.append( (1, 1) )
        visited[1][1] = 0
        step = 0
        #print("!!!")
        while True:
            #print("STEP", step)
            #print(q)
            newq = set()

            #assert len(q) > 0


            while len(q) > 0:
                curh, curw = q.pop()
                #print("new", curh, curw)

                if curh == oh and curw == ow:
                    print(step)
                    return

                if visited[curh][curw] < step: continue
                if maze[curh][curw] == INF: continue

                #print("!!!!!!!!!!!!!!!!!")
                #print("new", curh, curw)


                for di in range(len(dh)):
                    nh, nw = curh + dh[di], curw + dw[di]
                    if not (0 <= nh < len(maze)): continue
                    if not (0 <= nw < len(maze[0])): continue
                    if visited[nh][nw] != -1: continue  # 既に来たことがある
                    if maze[nh][nw] == INF: continue # 壊せない壁

                    if maze[nh][nw] == 0: # 通路の場合
                        visited[nh][nw] = step
                        q.append( (nh, nw) )
                        continue

                    if maze[nh][nw] == -1: # 壊せる壁の場合
                        #print("try bomb", nh, nw)
                        for ddh in range(-1, 2):
                            bh = nh + ddh
                            if not (0 <= bh < len(maze)): continue
                            for ddw in range(-1, 2):
                                bw = nw + ddw
                                if not (0 <= bw < len(maze[0])): continue
                                if maze[bh][bw] == -1:
                                    #print("bomb", bh, bw)
                                    newq.add( (bh, bw) )

            for nh, nw in newq:
                maze[nh][nw] = 0 # 通路にする
                visited[nh][nw] = step + 1
            q = list(newq)
            step += 1

        #pprint(parent)
        #pprint(maze)
        #print(parent[oh][ow])
        #pprint(maze)


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
        input = """5 5
..#..
#.#.#
##.##
#.#.#
..#.."""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 7
.......
######.
.......
.######
......."""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 8
.#######
########
########
########
########
########
########
#######."""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()