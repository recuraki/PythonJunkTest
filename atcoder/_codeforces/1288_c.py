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

    n, m = map(int, input().split())
    res = list(range(1, n+1))
    #print(res)
    for i in range(1, m):
        for j in range(1, n):
            res[j] += res[j-1]
        for j in range(1, n):
            res[j] += res[j - 1]
    for j in range(1, n):
        res[j] += res[j-1]
    print(res[-1] % 1000000007)



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
        input = """2 2"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 1"""
        output = """55"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """723 9"""
        output = """157557417"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()