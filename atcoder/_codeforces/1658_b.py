
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




    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    p = 998244353
    N = 20000  # N は必要分だけ用意する
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)


    def do():
        mod = 998244353
        n = int(input())
        if n%2 == 1:
            print(0)
            return
        ans = fact[n//2] **2
        ans %= mod
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
        input = """7
1
2
3
4
5
6
1000"""
        output = """0
1
0
4
0
36
665702330"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()