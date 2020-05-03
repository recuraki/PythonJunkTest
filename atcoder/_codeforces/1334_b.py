import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import bisect
    import collections

    q = int(input())
    for _ in range(q):
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        total = 0
        res = 0
        for i in range(n):
            cnt = i + 1
            total += dat[i]
            if total / cnt < x:
                break
            res = cnt
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
        input = """4
4 3
5 1 2 1
4 10
11 9 11 9
2 5
4 3
3 7
9 4 9"""
        output = """2
4
0
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()