import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, p = map(int, input().split())
    s = input()
    s = list(map(int, list(s)))
    #print(s)
    from collections import defaultdict
    res = defaultdict(int)
    from copy import deepcopy
    for i in range(n - 1, -1, -1):
        nres = defaultdict(int)
        c = s[i]
        keys = list(res.keys())
        print("c", c)
        print(keys)
        nres = deepcopy(res)
        for k in keys:
            nm = (c * 10 + k) % p
            nres[nm] += 1
        nres[c % p] += 1
        res = nres
        print("> end")
        print(res)

    print(res)




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
        input = """4 3
3543"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 2
2020"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 11
33883322005544116655"""
        output = """68"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()