import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    k = int(input())
    n = [a,b,c]
    n.sort()
    res = n[0] + n[1] + n[2] * pow(2,k)
    print(res)

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
        input = """5 3 11
1"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 3 4
2"""
        output = """22"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()