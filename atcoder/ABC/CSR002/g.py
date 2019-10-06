import sys
from io import StringIO
import unittest


def gcd (a,b):
    x,y = max(a,b), min(a,b)
    if x % y ==0:
        return y
    else:
        while x % y != 0:
            z = x % y
            x = y
            y = z
        else:
            return z

def resolve():
    import math
    import fractions
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(int(fractions.gcd(a,b)))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """4
6 15
20 19
240 240
555555555 999999999"""
        output = """3
1
240
111111111"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()