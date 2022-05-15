
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
        n, k,x  = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        #print(dat, x)
        # STEP1: k 円以下にする
        for i in range(n):
            if dat[i] < x: continue
            canuse = min(k, dat[i] // x)
            k -= canuse
            #print(i, dat[i], "use", canuse)
            dat[i] = max(dat[i] - canuse * x, 0)
            #print("so", dat[i])

        dat.sort(reverse=True)
        #print(dat, k, x)
        for i in range(n):
            if k <= 0: continue
            k -= 1
            dat[i] = 0
        print(sum(dat))


    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """5 4 7
8 3 10 5 13"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 100 7
8 3 10 5 13"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 815 60
2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202"""
        output = """112"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()