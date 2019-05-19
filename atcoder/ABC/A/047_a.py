import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    if (a+b) == c:
        print("Yes")
    elif (a+c) == b:
        print("Yes")
    elif (b+c) == a:
        print("Yes")
    else:
        print("No")

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
        input = """10 30 20"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """30 30 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """56 25 31"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()