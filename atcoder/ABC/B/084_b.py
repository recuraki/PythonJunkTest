import sys
from io import StringIO
import unittest

def resolve():
    a,b = map(int, input().split())
    s = input()
    f = True
    for i in range(len(s)):
        if i == a:
            continue
        if s[i] > "9" or s[i] < "0":
            f=False

    if s[a] != "-":
        f= False

    print("Yes" if f else "No")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test__1(self):
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)
    def test__2(self):
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)
    def test__3(self):
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()