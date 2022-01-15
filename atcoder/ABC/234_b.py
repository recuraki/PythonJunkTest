import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import math
    n = int(input())
    # 誤差のため、最後までsqrtはとらない
    diff = lambda a, b: (a[0]-b[0])**2 + (a[1]-b[1])**2 # paとpbの距離の大きさ
    cp1 = (-2000, -2000)
    cp2 = (-2000, +2000)
    cp3 = (+2000, -2000)
    cp4 = (+2000, +2000)
    cp5 = (0, 0)
    for i in range(n):
        p = tuple(map(int, input().split()))
        if diff((-2000, -2000), cp1) <= diff((-2000, -2000), p): cp1 = p
        if diff((-2000, +2000), cp2) <= diff((-2000, +2000), p): cp2 = p
        if diff((+2000, -2000), cp3) <= diff((+2000, -2000), p): cp3 = p
        if diff((+2000, +2000), cp4) <= diff((+2000, +2000), p): cp4 = p
        if diff((+000, +000), cp5) <= diff((+000, +000), p): cp5 = p
    ans = 0
    ans = max(ans, diff(cp1, cp2))
    ans = max(ans, diff(cp1, cp3))
    ans = max(ans, diff(cp1, cp4))
    ans = max(ans, diff(cp2, cp3))
    ans = max(ans, diff(cp2, cp4))
    ans = max(ans, diff(cp3, cp4))
    ans = max(ans, diff(cp5, cp1))
    ans = max(ans, diff(cp5, cp2))
    ans = max(ans, diff(cp5, cp3))
    ans = max(ans, diff(cp5, cp4))
    print(math.sqrt(ans))


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
        input = """3
0 0
0 1
1 1"""
        output = """1.4142135624"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
315 271
-2 -621
-205 -511
-952 482
165 463"""
        output = """1455.7159750446"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()