import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    if len(s) == 1:
        print(s + "1")
    else:
        count = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                print(s[i-1] + str(count), end="")
                count = 1
            else:
                count += 1
        print(s[len(s) - 1] + str(count))


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
        input = """aabbbaad"""
        output = """a2b3a2d1"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """aabbbbbbbbbbbbxyza"""
        output = """a2b12x1y1z1a1"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """edcba"""
        output = """e1d1c1b1a1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()