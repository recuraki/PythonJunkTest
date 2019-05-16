import sys
from io import StringIO
import unittest

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
        input = """600
300
220
420"""
        output = """520"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """555
555
400
200"""
        output = """755"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """549
817
715
603"""
        output = """1152"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    res = 0
    if a > b:
        res += b
    else:
        res += a
    if c > d:
        res += d
    else:
        res += c
    print(res)