import sys
from io import StringIO
import unittest

def resolve():
    s = input()
    m = 999
    for i in range(len(s) - 2):
        n = int(s[i+0]) *100 + int(s[i+1]) * 10 + int(s[i+2])
        m = min(abs(753 - n) ,m)
    print(m)


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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()