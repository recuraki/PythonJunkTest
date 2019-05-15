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
        input = """4 7 9 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100 10 1 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 10 10 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 100 2 10"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b,c,d = map(int, input().split())
    if (abs(a-b) <= d) and (abs(b-c) <= d):
        print("Yes")
    else:
        if (abs(a-c) <= d):
            print("Yes")
        else:
            print("No")

