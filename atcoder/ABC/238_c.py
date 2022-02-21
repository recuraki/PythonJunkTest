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
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        mod = 998244353
        s = str(n)

        # k = 1からnまでの k の和
        def sigma1(n):
            return n * (n + 1) // 2

        ans = 0
        for keta in range(1, len(s)):
            if keta < len(s): # その桁以下の場合
                x =  (10**keta -1 ) - 10**(keta-1) + 1
                ans += sigma1(x)
                ans %= mod
        keta = len(s)

        kazu = n - (10** (keta-1) ) + 1
        ans += sigma1(kazu)
        ans %= mod
        print(ans)

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
        input = """16"""
        output = """73"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """238"""
        output = """13870"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """999999999999999999"""
        output = """762062362"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()