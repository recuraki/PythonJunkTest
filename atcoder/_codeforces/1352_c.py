import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import math

    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        #print("n,k",n,k)
        x = math.ceil( (k-1) // (n - 1))
        res = n * x
        amari = k - ( (n-1) * x)
        #print("x,", x, "init", res, "amari", amari)
        res += amari
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
        input = """6
3 7
4 12
2 1000000000
7 97
1000000000 1000000000
2 1"""
        output = """10
15
1999999999
113
1000000001
1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_1")
        input = """8
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
"""
        output = """1
2
4
5
7
8
10
11"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()