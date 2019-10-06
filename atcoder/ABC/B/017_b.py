
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = input()
    res = True
    while len(x) > 0:
        if x[-1] == "o":
            x = x[:-1]
        elif x[-1] == "k":
            x = x[:-1]
        elif x[-1] == "u":
            x = x[:-1]
        elif len(x) > 1 and x[-1] == "h" and x[-2] == "c":
            x = x[:-2]
        else:
            res = False
            break
    print("YES" if res else "NO")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """chokuou"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """kuccho"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """atcoder"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()