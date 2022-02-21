import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    s = input()
    l = list(s)
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a], l[b] = l[b], l[a]
    print("".join(l))


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
        input = """chokudai
3 5"""
        output = """chukodai"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """aa
1 2"""
        output = """aa"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """aaaabbbb
1 8"""
        output = """baaabbba"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """a
1 1"""
        output = """a"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()