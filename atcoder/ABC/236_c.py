import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n, m = map(int, input().split())
        dats = list(input().split())
        datt = list(input().split())
        se = set(dats)
        for x in datt:
            se.remove(x)
        for x in dats:
            if x not in se: print("Yes")
            else: print("No")

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
        input = """5 3
tokyo kanda akiba okachi ueno
tokyo akiba ueno"""
        output = """Yes
No
Yes
No
Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 7
a t c o d e r
a t c o d e r"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()