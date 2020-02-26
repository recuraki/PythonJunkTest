import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = []
    import itertools
    for _ in range(n):
        x, y = map(int, input().split())
        dat.append((x,y))
    import math
    allsum = 0
    for a in itertools.permutations(range(n)):
        x, y = dat[a[0]]
        s = 0
        for b  in range(1, n):
            nx, ny = dat[a[b]]
            s += math.sqrt( (nx-x)**2 + (ny-y)**2 )
            x, y = nx, ny
        allsum += s
    res = allsum / math.factorial(n)
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
        input = """3
0 0
1 0
0 1"""
        output = """2.2761423749"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
-879 981
-866 890"""
        output = """91.9238815543"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310"""
        output = """7641.9817824387"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()