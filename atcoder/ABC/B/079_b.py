import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    l = []
    l.append(2)
    l.append(1)
    for i in range(1, n):
        l.append(l[-2] + l[-1])
    print(l[-1])



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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()