import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import math
    q = int(input())
    for _ in range(q):
        x = 1
        n = int(input())
        for i in range(100):
            x = (x << 1) + 1
            if n % x == 0:
                print(n // x)
                break

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
        input = """7
3
6
7
21
28
999999999
999999984"""

        output = """1
2
1
7
4
333333333
333333328"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()