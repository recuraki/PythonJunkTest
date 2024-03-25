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
        h1, h2, h3, w1,w2,w3 = map(int, input().split())
        sumh = [h1, h2, h3]
        sumw = [w1, w2, w3]
        def gen(x):
            ans = []
            for i in range(1, 30):
                for j in range(1, 30):
                    for h in range(1, 30):
                        if i + j + h == x:
                            ans.append((i, j, h))
            return ans

        can1 = gen(h1)
        can2 = gen(h2)
        can3 = gen(h3)
        ans = 0
        for pat1 in can1:
            for pat2 in can2:
                for pat3 in can3:
                    if pat1[0]+pat2[0]+pat3[0] != w1: continue
                    if pat1[1]+pat2[1]+pat3[1] != w2: continue
                    if pat1[2]+pat2[2]+pat3[2] != w3: continue
                    ans += 1
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
        input = """3 4 6 3 3 7"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4 5 6 7 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 13 10 6 13 9"""
        output = """120"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """20 25 30 22 29 24"""
        output = """30613"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()