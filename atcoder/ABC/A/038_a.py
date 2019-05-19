import sys
from io import StringIO
import unittest

def resolve():
    s = input()
    if s[-1] == "T":
        print("YES")
    else:
        print("NO")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """ICEDT"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """MUGICHA"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """OOLONGT"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """T"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例5(self):
        input = """TEA"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()