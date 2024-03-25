
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

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors


    def do():
        n, k = map(int, input().split())
        #print(n, k)
        s = input()
        divs = make_divisors(n)
        ans = n
        for div in divs:
            # divブロック に分解する
            need = 0
            chars = n // div # 各ブロックの文字数
            from collections import defaultdict
            #print("div", div)
            for char in range(chars): # offset
                #print(" char", char)
                cnt = defaultdict(int)
                for i in range(div): # iブロック目
                    cnt[s[i*chars + char]] += 1
                macnt = -1
                for ke in cnt.keys():
                    macnt = max(macnt, cnt[ke])
                need += div - macnt
            #print("div", div, "chars", chars, "need", need)
            if need <= k:
                ans = min(ans, chars)
        print(ans)

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
        input = """4 1
abac"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 0
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 1
abcaba"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()