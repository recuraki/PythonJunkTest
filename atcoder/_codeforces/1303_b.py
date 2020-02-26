import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    import math
    for _ in range(q):
        n, g, b = map(int, input().split())
        rg = math.ceil(n / 2) # 引くべき良い道
        rb = n - rg # 引くべき、どちらでもよい道
        res = 0
        needcycle = math.ceil(rg / g)  # 何回目で引き終わる？
        # 前まででどこまで引き終わった？
        rg = rg - (g * (needcycle - 1)) # 引かないといけない良い道
        rb = max(0, rb - b * (needcycle - 1)) # 引かないといけないどちらでもよい道
        # 必要な日数というのは 前のサイクルまでの日数＋最後のサイクルで必要な日数
        res = ((g + b) * (needcycle - 1)) + (rg + rb)
        print(res)




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
5 1 1
8 10 10
1000000 1 1000000"""
        output = """5
8
499999500000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()