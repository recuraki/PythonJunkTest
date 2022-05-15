
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, k = map(int, input().split())
        ans = 0
        dat = []
        for _ in range(n):
            dat.append(input())
        from collections import defaultdict
        for pat in range(2**n):
            tmp = defaultdict(int)
            canans = 0
            for i in range(n):
                # sxを選ぶ？
                if ((pat >> i) & 1) == 1:
                    for x in dat[i]: tmp[x] += 1
            for ke in tmp.keys():
                if tmp[ke] == k: canans += 1
            ans = max(ans, canans)
        print(ans)
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
        input = """4 2
abi
aef
bc
acg"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
a
b"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 2
abpqxyz
az
pq
bc
cy"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()