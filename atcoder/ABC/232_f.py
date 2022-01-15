import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import math
    INF = 1 << 63
    def do():
        n, x, y = map(int, input().split())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        from itertools import permutations
        for mapping in range

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
        input = """4 3 5
4 2 5 2
6 4 2 1"""
        output = """16"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 12345 6789
1 2 3 4 5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """18 20719114 5117250357733867
10511029 36397527 63027379 44706927 47672230 79861204 57882493 42931589 51053644 52300688 43971370 26515475 62139996 41282303 34022578 12523039 6696497 64922712
14720753 4621362 25269832 91410838 86751784 32741849 6602693 60719353 28911226 88280613 18745325 80675202 34289776 37849132 99280042 73760634 43897718 40659077"""
        output = """13104119429316474"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()