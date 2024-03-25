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
        #print("---------------------------")
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = list(map(lambda x: x % k, dat))
        ans = 0
        from collections import defaultdict
        cnt = defaultdict(list)
        for i in range(n):
            cnt[buf[i]].append(dat[i])
        l = 0
        r = k - 1
        while l <= r:
            if len(cnt[l]) == 0:
                l += 1
                continue
            if len(cnt[r]) == 0:
                r -= 1
                continue
            if (l + r) < k:
                l += 1
                continue
            if l == r and len(cnt[l]) == 1: break
            inda = cnt[l].pop()
            indb = cnt[r].pop()
            ans += (inda + indb) // k
            #print("YES!", inda, indb)
        nokori = []
        for i in range(k):
            while len(cnt[i]) > 0:
                nokori.append(cnt[i].pop())
        for i in range(0, len(nokori), 2):
            ans += (nokori[i] + nokori[i+1]) // k
            #print("YES?", nokori[i],  nokori[i+1])
        print(ans)



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
        input = """6
6 3
3 2 7 1 4 8
4 3
2 1 5 6
4 12
0 0 0 0
2 1
1 1
6 10
2 0 0 5 9 4
6 5
5 3 8 6 3 2"""
        output = """8
4
0
2
1
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()