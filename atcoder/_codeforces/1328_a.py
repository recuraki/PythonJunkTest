import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        c = b - a%b
        print(0 if c == b else c)


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
10 4
13 9
100 13
123 456
92 46"""
        output = """2
5
4
333
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()