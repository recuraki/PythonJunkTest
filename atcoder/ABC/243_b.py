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
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        ans1 = 0
        ans2 = 0
        for i in range(n):
            if data[i] == datb[i]: ans1 += 1
        for i in range(n):
            for j in range(n):
                if  i == j: continue
                if data[i] == datb[j]: ans2 += 1

        print(ans1)
        print(ans2)


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
        input = """4
1 3 5 2
2 3 1 4"""
        output = """1
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2 3
4 5 6"""
        output = """0
0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
4 8 1 7 9 5 6
3 5 1 7 8 2 6"""
        output = """3
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()