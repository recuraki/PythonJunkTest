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
        input = """3 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 2"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    a,b = map(int, input().split())
    flag = False
    if (a*b) % 2 == 1:
        flag = True
    if (a*b*3) % 2 == 1:
        flag = True
    if flag:
        print("Yes")
    else:
        print("No")
