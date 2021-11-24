import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
        import math
        n = int(input())



    do()



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
        input = """3
1 2
2 3
3 1"""
        output = """2 2 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1000000000 1000000000
1000000000 1000000000"""
        output = """0 1000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()