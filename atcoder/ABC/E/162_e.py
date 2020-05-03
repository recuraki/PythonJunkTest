import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import fractions
    import collections
    d = collections.defaultdict(int)
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            #print(i, j)
            x = fractions.gcd(i, j)
            d[x] += 1
    res = 0
    #print(d)
    for k in d:
        for i in range(1, n + 1):
            #print("gdc:", k, i , "=", fractions.gcd(k, i))
            x = fractions.gcd(k, i)
            res += x * d[k]
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
        input = """3 2"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 200"""
        output = """10813692"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000 100000"""
        output = """742202979"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()