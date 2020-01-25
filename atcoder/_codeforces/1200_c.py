import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m, q = map(int, input().split())
    import math
    g = math.gcd(n, m)
    g1 = n // g
    g2 = m // g
    #print("g={0}, g1={1}, g2={2}".format(g,g1,g2))
    for qq in range(q):
        a, b, c, d = map(int, input().split())
        if n == 1 or m == 1:
            print("YES")
            continue
        b,d = b-1, d-1
        #print("{0},{1},{2},{3}".format(a,b,c,d))
        if a == 1:
            area1 = math.floor(b / g1)
        else:
            area1 = math.floor(b / g2)
        if c == 1:
            area2 = math.floor(d / g1)
        else:
            area2 = math.floor(d / g2)
        #print("a1={0}, a2={1}".format(area1, area2))
        print("YES" if area1 == area2 else "NO")

class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """4 6 3
1 1 2 3
2 6 1 2
2 6 2 4"""
        output = """YES
NO
YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 12 3
2 1 2 3
2 1 2 4
2 6 2 4"""
        output = """YES
YES
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()