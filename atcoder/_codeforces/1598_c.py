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
        from collections import Counter
        n = int(input())
        dat = list(map(int, input().split()))
        res = 0
        C = Counter(dat)
        total = sum(dat)
        #print()
        if (total*2) % n != 0:
            print(0)
            return
        targetmean = (total*2) // n
        for x in dat:
            neednum = targetmean - x
            cnt = C[neednum]
            if neednum == x: cnt -= 1
            #print(x, "find", targetmean - x, "num=", cnt)
            res += cnt
        print(res // 2)

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
        input = """4
4
8 8 8 8
3
50 20 10
5
1 4 7 3 5
7
1 2 3 4 5 6 7"""
        output = """6
0
2
3"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
3
1 3 5"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()