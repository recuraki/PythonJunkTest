import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    t = [a,b,c]
    t.sort()
    print(t[1])
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
        input = """2 3 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """5 100 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """3 3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """3 3 4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()