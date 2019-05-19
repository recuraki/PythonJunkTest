import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    aa = max(a,b)
    bb = min(a,b)
    count = c / bb
    c -= count * bb
    if c >= aa:
        count += 1
    print(int(count))

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
        input = """3 5 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 6 20"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()