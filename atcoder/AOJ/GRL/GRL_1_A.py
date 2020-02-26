import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    v, e, r = map(int, input().split())
    for _ in range(e):




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
        input = """4 5 0
0 1 1
0 2 4
1 2 2
2 3 1
1 3 5"""
        output = """0
1
3
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 6 1
0 1 1
0 2 4
2 0 1
1 2 2
3 1 1
3 2 5"""
        output = """3
0
2
INF"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()