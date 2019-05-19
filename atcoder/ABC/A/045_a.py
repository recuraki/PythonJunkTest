import sys
from io import StringIO
import unittest

def resolve():
    a = int(input())
    b = int(input())
    h = int(input())
    print(int((a+b) * h / 2))
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
        input = """3
4
2"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
4
4"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()