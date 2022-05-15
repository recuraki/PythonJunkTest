import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

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
        cnt = [0] * 1000000
        for x in dat:
            a = 999999 - x
            cnt[a] += 1
        ans = 0
        for i in range(999999, -1, -1):
            s = str(i).zfill(6)
            for ind in range(6):
                if s[ind] == "0": continue
                ns = s[:ind] + str(int(s[ind])-1) + s[ind+1:]
                x = int(ns)
                cnt[x] += cnt[i]
        for x in dat:
            ans += cnt[x]
        print(ans)
        print(cnt)

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
4 8 12 90"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
313923 246114 271842 371982 284858 10674 532090 593483 185123 364245 665161 241644 604914 645577 410849 387586 732231 952593 249651 36908"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
1 1 1 1 1"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()