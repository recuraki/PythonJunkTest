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

    """
    make_divisors(16)
    # [1, 16, 2, 8, 4\]
    """

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors

    # 約数のリストを表示する(1とその数を除く)
    # ソートされていない
    """
    make_divisors_without_own(16)
    [2, 8, 4]
    """

    def make_divisors_without_own(n):
        r = make_divisors(n)
        r.remove(1)
        r.remove(n)
        return r



    def do():
        n, d = map(int, input().split())

        def isgood(num):
            return num % d == 0

        def isbeatuful(num):
            l = make_divisors(num)
            used = set()
            for x in l:
                y = num // x
                used.add(x)
                used.add(y)
                if isgood(x) and isgood(y):
                    return False
            return True
        from random import sample
        #n //= d
        #n //= d
        l = make_divisors(n)
        ans = set()
        for _ in range(1000000):
            s1 = sample(l, 1)[0]
            s2 = n//s1
            #print(s1, s2)
            if not isbeatuful(s1): continue
            if not isbeatuful(s2): continue
            z = [s1, s2]
            z.sort()
            z = tuple(z)
            ans.add(z)
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
        input = """1
16384 4"""
        output = """NO
NO
YES
NO
YES
YES
NO
YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()