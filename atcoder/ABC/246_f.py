import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, l = map(int, input().split())
        dat = []
        diff = []
        for _ in range(n):
            ll = list(input())
            ll.sort()
            dat.append(ll)
        ans = 0
        mod = 998244353
        for i in range(n):
            base = pow(len(dat[i]), l, mod)
            ans += base
        did = []
        for i in range(n):
            for j in range(i+1, n):
                x = set(dat[i]) & set(dat[j])
                ans -= pow(len(x), l, mod)
                for y in did:
                    ans += pow(len(x & y), l, mod)
                did.append(x)


        print(ans % mod)




    # 1 time
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
        input = """2 2
ab
ac"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
abcdefg
hijklmnop
qrstuv
wxyz"""
        output = """1352"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 1000000000
abc
acde
cefg
abcfh
dghi"""
        output = """346462871"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()