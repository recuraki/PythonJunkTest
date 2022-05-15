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




    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        dat = []
        n = int(input())
        from collections import defaultdict
        cnt = defaultdict(int)
        for _ in range(n):
            s = input()
            cnt[s] += 1
        for s in cnt.keys():
            a = ord(s[0]) - ord("a")
            b = ord(s[1]) - ord("a")
            dat.append( (a, b, cnt[s]) )
        n = len(dat)
        ans = 0
        for i in range(n):
            a1, a2, acnt = dat[i]
            for j in range(i + 1, n):
                b1, b2, bcnt = dat[j]
                if a1!=b1 and a2!=b2: continue
                ans += acnt * bcnt
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
        input = """4
6
ab
cb
db
aa
cc
ef
7
aa
bb
cc
ac
ca
bb
aa
4
kk
kk
ab
ab
5
jf
jf
jk
jk
jk"""
        output = """5
6
0
6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()