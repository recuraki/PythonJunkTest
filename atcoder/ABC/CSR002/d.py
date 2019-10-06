import sys
from io import StringIO
import unittest

def resolve():
    dat_a = []
    dat_b = []
    n = int(input())
    s = 0
    for i in range(n):
        a, b = map(int, input().split())
        s+= max(a,b)
    print(s)

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
        input = """2
20 19
1 100"""
        output = """120"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
123456789 987654321
999999999 999999999
1000000000 888888888"""
        output = """2987654320"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()