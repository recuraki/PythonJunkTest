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
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        cursor = 0
        curneed = dat[0]
        curman = 0
        res = 0
        while cursor < n:
            curneed = dat[cursor]
            curman += 1
            if curman >= curneed:
                res += 1
                curman = 0
            cursor += 1
        print(res)


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
5
2 2 2 2 2
5
1 1 1 1 1
5
6 6 6 6 6
5
5 5 5 5 5
5
2 3 1 2 2
2
1 2
1
2"""
        output = """2
5
0
1
2
1
0"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
5
1 2 4 4 4
"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()