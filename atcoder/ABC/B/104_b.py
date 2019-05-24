import sys
from io import StringIO
import unittest

def resolve():
    s  = input()
    f = True
    if s[0] != "A":
        f = False
    c = 0
    for i in range(2, len(s) - 1):
        if s[i] == "C":
            c += 1
    if c != 1:
        f=False
    ss = s[1:].replace("C", "")
    for i in range(len(ss)):
        if ss[i] < "a" or ss[i] > "z":
            f = False
    if f:
        print("AC")
    else:
        print("WA")


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
        input = """AtCoder"""
        output = """AC"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """ACoder"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """AcycliC"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """AtCoCo"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """Atcoder"""
        output = """WA"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


