import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline

    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        if n == 1:
            print(0)
            return
        last = dat[n - 1]
        print(n)
        for i in range(n - 1):
            last = min(last, dat[i])
            if i&1==0: print(i + 1, n, 1000000005, last)
            else:      print(i + 1, n, 1000000006, last)
        print(n - 1, n, 1000000007, last)
    q = int(input())
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
    def test_input_1(self):
        print("test_input_1")
        input = """3
5
9 6 3 11 15
3
7 5 13
4
1 2 3 4"""
        output = """2
1 5 11 9
2 5 7 6
0"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """3
2
1 2
2
1 2
2
1 2
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()