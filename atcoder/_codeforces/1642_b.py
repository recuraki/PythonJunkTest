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
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        from heapq import heappop, heappush, heapify
        n = int(input())
        dat = list(map(int, input().split()))
        se = set(dat)
        ans = len(se)
        res = [ans] * ans
        for i in range(n-ans):
            res.append(ans + i + 1)
        print(" ".join(list(map(str, res))))



    # n questions
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
        input = """2
3
1 1 2
6
5 1 2 2 2 4"""
        output = """2 2 3
4 4 4 4 5 6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
6
1 2 3 3 4 4"""
        output = """4 4 4 5 5 6"""
        self.assertIO(input, output)
    def test_input_2a(self):
        print("test_input_2")
        input = """1
6
1 2 3 4 5 6"""
        output = """6 6 6 6 6 6"""
        self.assertIO(input, output)

    def test_input_2aa(self):
        print("test_input_2aa")
        input = """1
6
1 1 1 1 1 1"""
        output = """1 2 3 4 5 6"""
        self.assertIO(input, output)
    def test_input_2aaa(self):
        print("test_input_2aaa")
        input = """1
1
1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2aaaa(self):
        print("test_input_2aaaa")
        input = """1
7
5 1 2 2 3 3 3
"""
        output = """4 4 4 5 5 6 7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()