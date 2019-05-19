import sys
from io import StringIO
import unittest

def resolve():
    n = input()
    if n[0]==n[1] and n[0]==n[2] and n[0]==n[3]:
        print("SAME")
    else:
        print("DIFFERENT")

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
        input = """2222"""
        output = """SAME"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1221"""
        output = """DIFFERENT"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """0000"""
        output = """SAME"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()