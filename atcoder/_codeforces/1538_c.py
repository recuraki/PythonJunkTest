import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    from bisect import bisect_right, bisect_left
    def do():
        n, l, r = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()
        res = 0
        for x in dat:
            targetl = l - x
            targetr = r - x
            indl = bisect_left(dat, targetl)
            indr = bisect_right(dat, targetr)
            cnt = indr - indl
            if l <= (x+x) <= r:
                cnt -= 1
            res += cnt
        print(res // 2)



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
        input = """4
3 4 7
5 1 2
5 5 8
5 1 2 4 3
4 100 1000
1 1 1 1
5 9 13
2 5 5 1 1"""
        output = """2
7
0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()