import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        import math
        def nCr(n, r):
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
        n = int(input())
        dat = []
        from collections import defaultdict
        cnt = defaultdict(int)
        for _ in range(n):
            x, y = map(int, input().split())
            dat.append( (x, y) )
        for i in range(n):
            p1 = dat[i]
            for j in range(i+1, n):
                p2 = dat[j]
                if p1[1] != p2[1]: continue # y軸が違うなら判定外
                # xについて、 p1<p2っぽくして、hashを取る
                if p1[0] >  p2[0]: x = p2[0] * (10 ** 9 + 7) + p1[0]  # hash
                else:              x = p1[0] * (10**9 + 7) + p2[0] # hash
                cnt[x] += 1
        res = 0
        # y軸が平行な、おなじ、xの範囲を持つ組み合わせをnCrする
        for k in cnt.keys():
            c = cnt[k]
            if c < 2: continue
            res += nCr(c, 2)
        print(res)

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
        input = """6
0 0
0 1
1 0
1 1
2 0
2 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
0 1
1 2
2 3
3 4"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
0 1
1 0
2 0
2 1
2 2
3 0
3 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """6
0 1
1 1
1 3
0 3
2 1
2 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_32")
        input = """8
3 0
1 0
3 1
1 1
3 2
1 2
4 1
5 2"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()