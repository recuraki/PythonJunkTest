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
    def do():
        def f(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        n, m, i, j = map(int, input().split())
        i -= 1
        j -= 1
        candidate = [(0,0), (0, m-1), (n-1, 0), (n-1, m-1)]
        cur = (i, j)
        from itertools import combinations
        resval = -1

        for l in combinations(candidate, 2):
            a, b = l[0], l[1]
            x = f(cur, a)
            x += f(a, b)
            x += f(b, cur)
            if x > resval:
                resval = x
                res = [a, b]
        print(res[0][0]+1, res[0][1]+1, res[1][0]+1, res[1][1]+1)

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
        input = """7
2 3 1 1
4 4 1 2
3 5 2 2
5 1 2 1
3 1 3 1
1 1 1 1
1000000000 1000000000 1000000000 50"""
        output = """1 2 2 3
4 1 4 4
3 1 1 5
5 1 1 1
1 1 2 1
1 1 1 1
50 1 1 1000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()