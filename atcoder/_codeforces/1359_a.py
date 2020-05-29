import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n, m, k = map(int, input().split())
        percard = n // k
        if m == n: # all joker
            print(0)
        elif m == 0: # joker = 0
            print(0)
        else: # other
            myjoker = min(percard, m)
            nokori = m - myjoker
            import math
            ojoker = math.ceil(nokori / (k-1))
            print(myjoker - ojoker)



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
8 3 2
4 2 4
9 6 3
42 0 7
8 8 2
8 0 2"""
        output = """3
0
1
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()