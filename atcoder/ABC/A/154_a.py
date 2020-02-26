import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s, t = input().split()
    a, b = map(int,input().split())
    u = input()
    d = dict()
    d[s] = a
    d[t] = b
    d[u] -= 1
    print("{0} {1}".format(d[s], d[t]))

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
        input = """red blue
3 4
red"""
        output = """2 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """red blue
5 5
blue"""
        output = """5 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()