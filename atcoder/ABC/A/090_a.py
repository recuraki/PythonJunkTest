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
        input = """ant
obe
rec"""
        output = """abc"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """edu
cat
ion"""
        output = """ean"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    c1 = input()
    c2 = input()
    c3 = input()
    print(c1[0] + c2[1] + c3[2])