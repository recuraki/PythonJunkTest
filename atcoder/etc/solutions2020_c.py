import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))

    prev = dat[0]

    for i in range(n-k):
        new = dat[k + i]
        nukeru = dat[i]
        if new > nukeru:
            print("Yes")
        else:
            print("No")
        prev = new

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
        input = """5 3
96 98 95 100 20"""
        output = """Yes
No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
1001 869120 1001"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """15 7
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9"""
        output = """Yes
Yes
No
Yes
Yes
No
Yes
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()