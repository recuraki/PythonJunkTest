import sys
from io import StringIO
import unittest

def resolve():
    w,h = map(int, input().split())
    if w/h == 4/3:
        print("4:3")
    else:
        print("16:9")

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
        input = """4 3"""
        output = """4:3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """16 9"""
        output = """16:9"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """28 21"""
        output = """4:3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()