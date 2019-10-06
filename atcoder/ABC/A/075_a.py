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
        input = """5 7 5"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 1 7"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """-100 100 100"""
        output = """-100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b,c = map(int, input().split())
    if(a == c ):
        print(b)
    if(a == b ):
        print(c)
    if(b == c ):
        print(a)
