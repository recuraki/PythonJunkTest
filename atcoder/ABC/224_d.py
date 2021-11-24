import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        m = int(input())
        g = [[] for _ in range(9)]

        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        dat = list(map(lambda x: int(x) - 1, input().split()))
        maze = [8] * 9
        for i in range(8):
            maze[dat[i]] = i
        aki = maze.index(8)

        def h(l):
            ans = 0
            for i in range(8, -1, -1):
                ans <<= 4
                ans += l[i]
            return ans

        targetans = h([0,1,2,3,4,5,6,7,8])
        ha = h(maze)
        if ha == targetans:
            print(0)
            return
        #print(bin(targetans))

        from collections import deque
        q = deque()
        res = 2**31
        q.append( (ha, aki, 0) ) # map, akiの位置, Round
        known = set()
        cnt = 0
        while len(q) > 0:
            curha, aki, round = q.popleft()
            if curha in known: continue
            known.add(curha)
            cnt += 1
            for candidatenode in g[aki]:
                akinum = 0b1000
                cannum = (curha >> (4 * candidatenode) ) & 0b1111
                nextha = curha
                nextha ^= (akinum << (4 * aki) )
                nextha ^= (cannum << (4 * candidatenode) )
                nextha ^= (akinum << (4 * candidatenode))
                nextha ^= (cannum << (4 * aki))
                if nextha in known: continue
                known.add(ha)
                if nextha == targetans:
                    print(round+1)
                    return
                q.append( (nextha, candidatenode, round + 1) )
        if res == 2**31: res = -1
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
        input = """5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2
1 3
1 9
2 9
3 9
1 2 3 4 5 6 7 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """12
8 5
9 6
4 5
4 1
2 5
8 9
2 1
3 6
8 7
6 5
7 4
2 3
1 2 3 4 5 6 8 7"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """12
6 5
5 4
4 1
4 7
8 5
2 1
2 5
6 9
3 6
9 8
8 7
3 2
2 3 4 6 1 9 7 8"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()