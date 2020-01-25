import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    import math
    import collections
    for qq in range(q):
        n = int(input())
        res = collections.deque([])
        t = n
        last = -1
        for i in range(1, n):
            t *= (i / (i + 1))
            if last != math.floor(t):
                last = math.floor(t)
                res.append(last)
        l = list(map(str, res))
        print(len(l))
        print(" ".join(l))

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
        input = """4
5
11
1
3"""
        output = """4
0 1 2 5
6
0 1 2 3 5 11
2
0 1
3
0 1 3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()

