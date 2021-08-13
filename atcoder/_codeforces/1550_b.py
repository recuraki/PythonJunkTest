import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():



    from pprint import pprint
    def do():
        import itertools

        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]


        n, a, b = map(int, input().split())
        s = input()
        c = countstrs(s)
        cn = len(c)
        score1 = (a + b) * n
        kai = (cn + 2) // 2
        score2 = a * n + b * kai
        print(max(score1, score2))
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
3 2 0
000
5 -2 5
11001
6 1 -4
100111"""
        output = """6
15
-2"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """1
1 1 -1
0
"""
        output = """"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()