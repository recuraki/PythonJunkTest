import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    f = True
    for i in range(n):
        c = dat[i]
        if c%2 == 0:
            if c%3 ==0 or c%5==0:
                pass
            else:
                f = False
    print("APPROVED" if f else "DENIED")

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
        input = """5
6 7 9 10 31"""
        output = """APPROVED"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
28 27 24"""
        output = """DENIED"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()