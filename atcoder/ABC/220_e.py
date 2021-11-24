import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63

    def do():
        import math
        mod = 998244353
        n, d = map(int, input().split())
        res = [0] * n
        res[0] = pow(2, n, mod)
        print()
        for i in range(0, n):
            a = i
            b = d - i
            x = (pow(2, a, mod)) # 対象となるノードの数
            y = (pow(2, b, mod) ) # 相手の候補
            print(i, x, y)
            res[i] = x * y
            res[i] %= mod
        print(res)
        #print(sum(res) % mod)

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
        input = """3 2"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """14142 17320"""
        output = """11284501"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()