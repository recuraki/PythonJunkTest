import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, x = map(int, input().split())

        class LIS():
            res = []
            INF = 1 << 61
            longestlen = -1

            def __init__(self):
                pass

            def load(self, l):
                self.longestlen = -1
                from bisect import bisect_left
                self.res = [self.INF] * (len(l) + 1)
                for x in l:
                    ind = bisect_left(self.res, x)
                    self.res[ind] = x
                    self.longestlen = max(self.longestlen, ind + 1)
                self.res = self.res[:self.longestlen]

            def load_sameok(self, l):
                self.longestlen = -1
                from bisect import bisect_left, bisect_right
                self.res = [self.INF] * (len(l) + 1)
                for x in l:
                    ind = bisect_right(self.res, x)
                    self.res[ind] = x
                    self.longestlen = max(self.longestlen, ind + 1)
                self.res = self.res[:self.longestlen]
        ansnum = -1
        ans = []

        def f(n, x, start, initdelta):
            visited = [False] * (n + 1)
            visited[0] = True
            visited[x] = True
            assert x != start
            dat = [x, start]
            cur = start
            while True:
                nxt = cur - initdelta
                over = True
                if 0 < nxt <= n:
                    over = False
                    if visited[nxt] is False:
                        visited[nxt] = True
                        dat.append(nxt)
                        cur = nxt
                        initdelta += 1
                        continue
                nxt = cur + initdelta
                if 0 < nxt <= n:
                    over = False
                    if visited[nxt] is False:
                        visited[nxt] = True
                        dat.append(nxt)
                        cur = nxt
                        initdelta += 1
                        continue
                initdelta += 1
                #print("loop", over, visited)
                if over: break
            l = []
            for i in range(len(dat) - 1):
                l.append(abs(dat[i] - dat[i + 1]))
            lis = LIS()
            lis.load(l)
            return dat, lis.longestlen
        did = set()
        for initdelta in range(1, 2, 3):
            for delta in range(10):
                for start in (delta, n-delta, x-delta, x+delta):
                    if start in did: continue
                    did.add(start)
                    if start == x: continue
                    if not (1 <= start <= n): continue
                    can, lele = f(n, x, start, x)
                    if lele > ansnum:
                        ansnum = lele
                        ans = can
        se = set()
        for x in ans:
            se.add(x)
        for i in range(1, n+1):
            if i not in se:
                ans.append(i)

        print(*ans)

    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """3 2"""
        output = """2 1 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 1"""
        output = """1 2 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()