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
        input = """kyoto
tokyo"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """abc
arc"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """aaaaaaaaaaaaaaab
aaaaaaaaaaaaaaab"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    s = input()
    t = input()
    ok = False
    for i in range(len(s)):
        if s == t:
            ok = True
            break
        s = s[-1] + s[0:-1]

    if ok:
        print("Yes")
    else:
        print("No")
