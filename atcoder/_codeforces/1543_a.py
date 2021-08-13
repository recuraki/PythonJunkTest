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




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math
    def do():
        a,b = map(int, input().split())
        if a == b:
            print(0, 0)
            return
        a, b = min(a,b), max(a,b)

        cnt = 0
        maxval = math.gcd(a,b)
        diff = b - a
        rescnt = min(a % diff, diff - (a%diff))
        print(diff, rescnt)


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
8 5
1 2
4 4
3 9"""
        output = """3 1
1 0
0 0
6 3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()