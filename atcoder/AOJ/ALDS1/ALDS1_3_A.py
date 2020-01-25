import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    d = collections.deque([])
    dat = input().split()
    for i in range(len(dat)):
        if dat[i] == "+":
            d.append(int(d.pop()) + int(d.pop()))
        elif dat[i] == "-":
            d.append(-int(d.pop()) + int(d.pop()))
        elif dat[i] == "*":
            d.append(int(d.pop()) * int(d.pop()))
        else:
            d.append(int(dat[i]))
    print(d.pop())


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
        input = """1 2 +"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2 + 3 4 - *"""
        output = """-3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()