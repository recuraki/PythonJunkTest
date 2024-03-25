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
        # k = 1からnまでの k の和 (include)

        n, k = map(int, input().split())
        dat = list(map(int, input().split()))

        def f(dat,n, k):
            ans = 0
            if n == 1:
                ans = dat[0] + (k - 1)
                print(ans)
                return
            dat.sort(reverse=True)
            for i in range(min(k, n)):
                ans += dat[i] + i
            k -= min(k, n)
            #print("nokori", k)
            ans += (n - 0) * (k)
            return(ans)

        def func(mid):
            ran = n - (mid-1)
            l = []
            for i in range(ran):
                l.append(f(dat[i:i+mid], mid, k))



        ok = 0
        ng = n
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            m = func(mid)
            if (func(mid - 1) <= m and  m >=  func(mid + 1)):
                ok = mid;
            else:
                ng = mid;
        print(ok)

    # n questions
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
5 2
5 6 1 2 3
5 7
5 6 1 2 3
1 2
999999
5 70000
1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """12
37
1000000
5000349985"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
2 6
10 0"""
        output = """19"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()