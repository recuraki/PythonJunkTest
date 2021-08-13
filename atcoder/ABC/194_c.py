import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        import collections

        n = int(input())
        dat = list(map(int, input().split()))
        d = collections.defaultdict(int)
        for i in range(n):
            d[dat[i]] += 1
        keys = list(d.keys())
        keys.sort()
        #print(keys)
        res = 0
        l = len(keys)
        for i in range(l):
            numi = keys[i]
            counti = d[numi]
            for j in range(i+1, l):
                numj = keys[j]
                countj = d[numj]
                #print(numi, counti, numj, countj)
                x = (numi - numj) ** 2
                res += x * (counti * countj)
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
2 8 4"""
        output = """56"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()