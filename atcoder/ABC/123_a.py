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
        input = """1
2
4
8
9
15"""
        output = """Yay!"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """15
18
26
35
36
18"""
        output = """:("""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (max(a,b,c,d,e) - min(a,b,c,d,e)) > k:
        print(":(")
    else:
        print("Yay!")
