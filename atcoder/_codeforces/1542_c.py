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
    mod = 10**9 + 7
    def do():
        n = int(input())
        import math
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)
        x = 1
        res = 2 * n
        for i in range(2, 41):
            x = lcm(x, i)
            cnt = n // x
            res = res - (i-1)*cnt + (i) * cnt
        print(res% mod)


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
        input = """6
1
2
3
4
10
10000000000000000"""
        output = """2
5
7
10
26
366580019"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()