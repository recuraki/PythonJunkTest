import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, l = map(int, input().split())
    dat_s = []
    for i in range(n):
        s = input()
        dat_s.append(s)
    dat_s.sort()
    print("".join(dat_s))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3 3
dxx
axx
cxx"""
        output = """axxcxxdxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()