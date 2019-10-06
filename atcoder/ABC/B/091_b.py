import sys
from io import StringIO
import unittest

def resolve():
    ad = {}
    mi = {}

    n = int(input())
    for i in range(n):
        s = input()
        n = ad.get(s, 0)
        n += 1
        ad[s] = n

    n = int(input())
    for i in range(n):
        s = input()
        n = mi.get(s, 0)
        n += 1
        mi[s] = n

    res = 0
    for k in ad.keys():
        val = ad[k]
        val -= mi.get(k, 0)
        res = max(res, val)

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
    def test_入力例_1(self):
        input = """3
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
apple
orange
apple
5
apple
apple
apple
apple
apple"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()