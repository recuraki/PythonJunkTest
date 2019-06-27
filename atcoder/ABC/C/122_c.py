import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, q = map(int, input().split())
    s = input()
    dat_q = []
    for i in range(q):
        l, r = map(int, input().split())
        dat_q.append((l, r))

    c = [0] * n
    for i in range(1, n):
        if s[i-1:i+1] == "AC":
            c[i] = c[i-1] + 1
        else:
            c[i] = c[i-1]
    for i in range(q):
        l, r = dat_q[i][0], dat_q[i][1]
        print(c[r - 1] - c[l - 1])
"""
ACACTACG
01122233

  ACTAC
  
"""

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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()