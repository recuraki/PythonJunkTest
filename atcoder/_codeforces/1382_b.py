import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools
    def countint(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]

    q = int(input())
    import collections

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = countint(dat)
        turn1 = True
        num, cnt = buf[0]
        if len(buf) == 1: # 1 only
            if num == 1 and cnt &1 == 0:
                print("Second")
            else:
                print("First")
        else:
            if num == 1 and cnt &1 == 1:
                print("Second")
            else:
                print("First")

    for _ in range(q):
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
    def test_input_11(self):
        print("test_input_11")
        input = """2
6
1 1 2 1 2 2
5
1 2 2 1 1"""
        output = """First
Second"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """7
3
2 5 4
8
1 1 1 1 1 1 1 1
6
1 2 3 4 5 6
6
1 1 2 1 2 2
1
1000000000
5
1 2 2 1 1
3
1 1 1"""
        output = """First
Second
Second
First
First
Second
First"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()