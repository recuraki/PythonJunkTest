import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    INF = 1 << 63
    def do():
        from collections import deque

        dh = [0, -1, 1, 0]
        dw = [-1, 0, 0, 1]

        n = int(input())
        k = int(input())
        ok = k
        maze = []
        oh, ow = n, n
        maze.append( ["#"] * (n+2))
        for h in range(oh):
            l = input()
            l = list(l)
            l = ["#"] + l + ["#"]
            maze.append(l)
        maze.append( ["#"] * (n+2))
        oh, ow = n+2, n+2
        visited = [[False] * ow  for _ in range(oh)]
        hash = set()
        candidate = set()
        did = set()

        hw2num = lambda hhh, www:        1 << (10*(hhh) + (www))
        num2hw = dict()
        for h in range(11):
            for w in range(11):
                num2hw[hw2num(h, w)] = (h, w)

        def f(h, w, k):
            if maze[h][w] == "#": return 0 # 壁なら即座に終わり
            if visited[h][w]: return 0 # このループで訪ねているなら終わり
            #print(h, w, k)

            visited[h][w] = True

            curhash = 0
            cnt = 0
            for hhh in range(n):
                for www in range(n):
                    if visited[1+hhh][1+www]:
                        cnt += 1
                        curhash |= 1 << (8*hhh + www)

            if curhash in did:
                visited[h][w] = False
                return 0
            did.add(curhash)

            if k == 1: # +1したいところ
                if cnt != ok: return
                hash.add(curhash)
                visited[h][w] = False
                return

            currentCandidate = set()

            for di in range(len(dh)):
                nh, nw = h + dh[di], w + dw[di]
                if maze[nh][nw] == "#": continue
                if visited[nh][nw]: continue
                nextnum = hw2num(nh, nw)
                if nextnum in candidate: continue # もう入っているなら候補にしない
                currentCandidate.add(nextnum)
                candidate.add(nextnum)

            for ncan in candidate:
                nh, nw = num2hw[ncan]
                f(nh, nw, k - 1)

            for key in currentCandidate: candidate.remove(key)
            visited[h][w] = False

        for h in range(oh):
            for w in range(oh):
                #print("!", h, w)
                if maze[h][w] == "#": continue
                if visited[h][w]: continue
                f(h, w, k)
                #maze[h][w] = "#" # 埋める

        print(len(hash))
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

    def test_input_0(self):
        print("test_input_0")
        input = """2
2
..
.."""
        output = """4"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """3
5
#.#
...
..#"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
2
#.
.#"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
8
........
........
........
........
........
........
........
........"""
        output = """64678"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """3
1
...
...
..."""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()