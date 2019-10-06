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
        input = """4 5"""
        output = """Possible"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 1"""
        output = """Impossible"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b = map(int, input().split())
    if (a) % 3 == 0 or b%3==0 or(a+b)%3==0:
        print("Possible")
    else:
        print("Impossible")