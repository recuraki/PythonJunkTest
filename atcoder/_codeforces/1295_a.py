import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)

    md = 998244353
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            res = "1" * (n // 2)
        else:
            res = "1" * (n // 2)
            l = list(res)

            l[0] = "7"
            res="".join(l)
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
        input = """2
3
4"""
        output = """7
11"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()