import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for qq in range(q):
        n, s, k = map(int, input().split())
        dat = list(map(int, input().split()))
        res = 0
        while True:
            if (s + res) not in dat and (s + res) <= n: break
            if (s - res) not in dat and (s - res) >= 1: break
            res += 1
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
        input = """1
5 5 3
1 3 5
"""
        output = """1"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()