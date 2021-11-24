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
    mod = 998244353
    def do():
        class Bit:
            def __init__(self, n):
                self.size = n
                self.tree = [0] * (n + 1)

            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

            def add(self, i, x):
                while i <= self.size:
                    self.tree[i] += x
                    i += i & -i

        import math
        n = int(input())
        dat = list(map(int, input().split()))
        zatsu = sorted(set(dat))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newl = []
        for x in dat:
            newl.append(zatsuTable[x])
        dat = newl
        print(dat)
        bit = Bit(n)
        def ss(p, aa):
            x = bit.sum(p) - bit.sum(p-1)
            bit.add(-x)
            bit.add(aa)

        for x in dat:
            bit.add(x + 1, 1)
        res = 0

        for i in range(n):
            x = dat[i] + 1
            bigcount = bit.sum(n) - bit.sum(x-1) - 1
            res += pow(2, bigcount, mod)
            res -= 1
            res %= mod
            print(res, bigcount)
            bit.add(x, -1)
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
        input = """3
1 2 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
3 2 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10
198495780 28463047 859606611 212983738 946249513 789612890 782044670 700201033 367981604 302538501"""
        output = """830"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """2
1 2"""
        output = """0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()