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
        """
        0: h, wが一緒
        1: hのみが一緒
        2: wのみが一緒
        3: xもyも違う
        """
        # コーナーケースは異常
        mod = 998244353
        h, w, k = map(int, input().split())
        a, b, c, d = map(int, input().split()) # h1, w1, h2, w2
        c0 = c1 = c2 = c3 = 0
        if a == c and b == d: c0 = 1
        elif a == c : c1 = 1
        elif b == d : c2 = 1
        else: c3 = 1
        #if k > 100: return
        for i in range(k):
            #print(i, c0, c1,c2,c3)
            n0 = (c1 + c2)
            n1 = (c0 * (w-1)) + c3 + (c1 * (w - 2)) # 1: hのみが一緒
            n2 = (c0 * (h-1)) + c3 + (c2 * (h - 2))# 2: wのみが一緒
            n3 = (c1 * (h -1)) + (c2 * (w - 1)) + (c3 * (h-2)) + (c3 * (w-2))# 3: xもyも違う
            n0 %= mod
            n1 %= mod
            n2 %= mod
            n3 %= mod
            c0, c1, c2, c3 = n0, n1, n2, n3
        #print(i, c0, c1,c2,c3)
        print(c0 % mod)
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
        input = """2 2 2
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000"""
        output = """24922282"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 3 3
1 3 3 3"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()