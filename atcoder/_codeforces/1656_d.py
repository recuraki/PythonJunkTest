
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

    # k = 1からnまでの k の和 (include)
    def sigma1(n):
        return n * (n + 1) // 2
    def f(n, i):
        x = n - sigma1(i)
        if n < sigma1(i): return False
        if x % i == 0: return True
        return True # n > s
    def f2(n, i):
        x = n - sigma1(i)
        if n < sigma1(i): return False
        if x % i == 0: return True
        return False # n > s



    ngg= set()
    for i in range(10**10):
        ngg.add(2**i)
        if 2**i > 10**20:
            break
    def do():
        n = int(input())
        if n in ngg:
            print("-1")
            return

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        ok = 0
        ng = 10**5 + 1
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if(f(n, mid)) :ok = mid;
            else : ng = mid;
        for i in range(ok - 10, ok + 10):
            if i < 2: continue
            if f2(n, i):
                print(i)
                return



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
        input = """5
2
4
6
15
20"""
        output = """-1
-1
3
3
5"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
121"""
        output = """"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()