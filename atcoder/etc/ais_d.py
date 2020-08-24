import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def popcount(i):
        assert 0 <= i < 0x100000000
        i = i - ((i >> 1) & 0x55555555)
        i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
        return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
    memo = [None] * 300000
    def do2(x):
        if memo[x] is not None:
            return memo[x]
        cnt = 0
        while x != 0:
            x = x % popcount(x)
            cnt += 1
        memo[x] = cnt
        return cnt

    def do():
        ll = int(input())
        s = input()
        n = int(s, 2)

        x = n
        cnt = 0
        ss = bin(x)[2:]
        cnt += 1
        num1 = ss.count("1")
        num1m = num1 - 1
        num1p = num1 + 1
        rs = ss[::-1]
        res1m = 0
        res1p = 0
        for j in range(len(rs)):
            if rs[j] == "1":
                if num1m != 0 and num1m != -1:
                    res1m += pow(2, j, num1m)
                    res1m %= num1m
                res1p += pow(2, j, num1p)
                res1p %= num1p

        #print(res1m, res1p, num1m, num1p)
        for i in range(len(s)):
            #print("i", i)
            if s[i] == "1": # 0になるから
                #print("down")
                #print(res1m, pow(2, ll - i -1, num1m))
                if num1m == 0 or num1m == -1:
                    print(0)
                    continue
                x = res1m - pow(2, ll - i -1, num1m)
                x %= num1m
            elif s[i] == "0": # 1になるから
                #print("up")
                #print(res1p, pow(2, ll - i -1, num1p))
                x = res1p + pow(2, ll - i-1, num1p)
                x %= num1p

            if x == 0:
                print(1)
                continue
            print(do2(x) + 1)
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
        input = """3
001"""
        output = """2
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()