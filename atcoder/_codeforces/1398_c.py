import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import Counter
    q = int(input())
    for _ in range(q):
        n,s = int(input()),input()
        dat = [0] * (n + 1)
        # Cumulative sum
        for i in range(n):
            dat[i+1] = dat[i] + (int(s[i]) - 1)
        c = Counter(dat)
        res = 0
        for k in c.keys():
            if c[k] < 2:
                pass
            x = c[k] - 1
            res += x * (x+1) // 2
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
3
120
5
11011
6
600005"""
        output = """3
6
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()