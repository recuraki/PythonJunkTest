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

        def factorization(n):
            factors = []

            if n == 1:
                return []

            while n % 2 == 0:
                factors.append(2)
                n //= 2

            i = 3
            while i ** 2 <= n:
                while n % i == 0:
                    factors.append(i)
                    n //= i
                i += 2

            if n != 1:
                factors.append(n)

            return factors
        oa,ob, ok = map(int, input().split())
        from collections import deque

        a = factorization(oa)
        b = factorization(ob)
        if 1 in a:
            a.remove(1)
        if 1 in b:
            b.remove(1)

        unimin = 0
        if len(a) > 0: unimin += 1
        if len(b) > 0: unimin += 1
        if unimin <= ok <= ( len(a) + len(b) ):
            print("YES")
            return
        print("NO")


    q = int(input())
    for _ in range(q):
        do()
    # do()





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
        input = """8
36 48 2
36 48 3
36 48 4
2 8 1
2 8 2
1000000000 1000000000 1000000000
1 2 1
2 2 1"""
        output = """YES
YES
YES
YES
YES
NO
YES
NO"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1
1 1 1
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()