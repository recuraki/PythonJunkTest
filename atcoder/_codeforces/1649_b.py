
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        r = n-1
        if dat.count(0) == n:
            print(0)
            return
        for l in range(n):
            if dat[l] == 0: continue
            if dat[l] == 1:
                dat[l] = 0
                continue
            if l >= r: break
            while dat[l] > 1:
                canusel = dat[l] - 1
                if l >= r: break
                while dat[r] > 0:
                    use = min(canusel, dat[r])
                    dat[l] -= use
                    dat[r] -= use
                r -= 1
            if l >= r: break

        if sum(dat) == 0:
            print(1)
            return
        if dat.count(1) == 2:
            print(1)
            return
        print(1 + sum(dat)-1)

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

    def test_input_11(self):
        print("test_input_11")
        input = """4
4
2 3 3 2
3
1 5 2
2
0 0
4
1000000000 1000000000 1000000000 1000000000"""
        output = """1
2
0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()