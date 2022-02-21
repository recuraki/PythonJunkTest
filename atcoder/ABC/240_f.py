import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        # a:初項, 公差d, 項数n, 末項lの 1-nまでの和
        def sigma4(a, d, n, l):
            return (n*(a+l)) // 2
            return n * (2 * a + (n - 1) * d) // 2
        n, m = map(int, input().split())
        dat = []
        for _ in range(n):
            a, b = map(int, input().split())
            dat.append( (a, b) )

        ans = dat[0][0]
        pb = 0
        pc = 0
        for a, b in dat:
            nb = pb + (a*b) # 末項
            tb = pb + (a) # 初項
            # b =項数
            # a = 公差
            tc = pc + pb + a
            nc = pc + sigma4(tb, a, b, nb)
            ans = max(ans, nc, tc)
            #print(pb, pc, nb, nc)
            pb = nb
            pc = nc

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
        input = """3
3 7
-1 2
2 3
-3 2
10 472
-4 12
1 29
2 77
-1 86
0 51
3 81
3 17
-2 31
-4 65
4 23
1 1000000000
4 1000000000"""
        output = """4
53910
2000000002000000000"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
3 7
-1 2
2 3
-3 2"""
        output = """4"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()