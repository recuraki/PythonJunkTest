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
        n, m = map(int, input().split())
        dat = []
        minforce = [-INF] * (n+1) # maxで更新する
        maxlimit = [INF] * (n+1)  # minで更新する
        buf = [0] * (n + 1)
        from collections import defaultdict
        minforce[0] = 0
        event = defaultdict(list)
        eventr = defaultdict(list)
        for _ in range(m):
            l, r = map(int, input().split())
            event[l].append(r)
            eventr[r].append(l)
        for l in range(1, n+1): # left
            cur = buf[l-1] + 1 # できれば大きくなりたい
            if minforce[l] != -INF: cur = min(cur, minforce[l])
            if maxlimit[l] !=  INF: cur = min(cur, maxlimit[l])
            buf[l] = cur
            # right
            for r in event[l]:
                dist = (r-l+1)//2
                center = r - dist # 中央となる位置
                minforce[r] = cur
                maxlimit[center] = cur + dist
        #for i in range(n+1):
        #    if i not in eventr :
        #        buf[i] = None
        print("min", minforce)
        print("max", maxlimit)
        print("buf", buf)
        # 逆にたどる？
        for r in range(n-1, -1, -1): # left
            cur = buf[r + 1] - 1 # できれば大きくなりたい
            if minforce[r] != -INF: cur = max(cur, minforce[r])
            if maxlimit[r] !=  INF: cur = min(cur, maxlimit[r])
            buf[r] = cur
            # right
            for l in eventr[r]:
                dist = (r-l+1)//2
                center = r - dist # 中央となる位置
                minforce[l] = cur
                maxlimit[center] = cur + dist
        print("min", minforce)
        print("max", maxlimit)
        print("buf", buf)





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
        input = """4 2
1 2
3 4"""
        output = """0101"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 2
1 4
3 6"""
        output = """001100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 10
6 17
2 3
14 19
5 14
10 15
7 20
10 19
3 20
6 9
7 12"""
        output = """00100100101101001011"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()