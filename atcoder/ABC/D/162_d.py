import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def nCr(n, r):
        import math
        # nCrのr>nは組み合わせが存在しないので0を返す
        # raiseすべきのこともあるかも
        if r > n:
            return 0
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

    n = int(input())
    s = input()
    tr, tg, tb = 0,0,0
    for i in range(n):
        if s[i] == "R":
            tr  += 1
        if s[i] == "G":
            tg  += 1
        if s[i] == "B":
            tb  += 1

    total = tr*tg*tb
    # same color
    #total -= nCr(tr, 3)
    #total -= nCr(tg, 3)
    #total -= nCr(tb, 3)
    #print(nCr(n, 3), nCr(tr, 3), nCr(tg, 3), nCr(tb, 3))
    #print(total)
    # cond 2
    for i in range(1, n):
        for j in range(1, min(i, n-i-1) + 1):
            a,b,c = s[i-j], s[i], s[i+j]
            if a != b and b != c and a != c:
                total -= 1
    print(total)


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
        input = """4
RRGB"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
RRRRRRR"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()