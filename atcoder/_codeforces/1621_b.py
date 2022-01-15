import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math
    INF = 1 << 63
    def do():
        from collections import defaultdict
        specialcost = defaultdict(lambda :defaultdict(lambda :INF)) # l, rを1つでカバーする最小のコスト
        cost = defaultdict(lambda : INF) # その点をカバーする最小のコスト
        n = int(input())
        dat = []
        for _ in range(n):
            dat.append( map(int, input().split()) )
        curl, curr = INF, -INF
        for i in range(n):
            l, r, c = dat[i]
            specialcost[l][r] = min(specialcost[l][r], c)
            curl, curr = min(l, curl), max(r, curr)
            cost[l], cost[r] = min(cost[l], c), min(cost[r], c)
            print(min(cost[curl] + cost[curr], specialcost[curl][curr]))

    q = int(input())
    for _ in range(q):
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
        input = """3
2
2 4 20
7 8 22
2
5 11 42
5 11 42
6
1 4 4
5 8 9
7 8 7
2 10 252
1 11 271
1 10 1"""
        output = """20
42
42
42
4
13
11
256
271
271"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
1
2 4 20
"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()