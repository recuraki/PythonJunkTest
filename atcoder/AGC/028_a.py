import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import fractions
    def lcm(x, y):
        return (x * y) // fractions.gcd(x, y)

    n, m = map(int, input().split())
    s = input()
    t = input()
    d = dict()
    f = True

    g = lcm(n, m)
    nn = g // n
    mm = g // m

    for i in range(n):
        d[1 + nn * i] = s[i]

    for i in range(m):
        if 1+mm*i in d:
            if d[1+mm * i] != t[i]:
                f = False
    if f:
        print(g)
    else:
        print(-1)


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
        input = """3 2
acp
ae"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 3
abcdef
abc"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """15 9
dnsusrayukuaiia
dujrunuma"""
        output = """45"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()