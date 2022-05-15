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
        if n == 2:
            print(min(dat))
            return
        finalres = INF

        ans = [INF] * n
        ans[0] = dat[-1]
        ans[1] = dat[0]
        for i in range(2, n):
            ans[i] = min(ans[i], ans[i-2] + dat[i-1]) # Pat1
            ans[i] = min(ans[i], ans[i-1] + dat[i-1]) # Pat2
            ans[i] = min(ans[i], ans[i-1] + dat[i]) # Pat3
        finalres = min(finalres, ans[n-1])


        print(finalres)

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
        input = """5
2 5 3 2 5"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62"""
        output = """426"""
        self.assertIO(input, output)

    def test_input_21(self):
        print("test_input_21")
        input = """2
10 20"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()