import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def prime_list_eratosthenes(n):
        import math
        if n == 1:
            return []
        if n == 2:
            return [2]
        prime = [2]
        limit = math.sqrt(n)
        data = [i + 1 for i in range(2, n, 2)]
        while True:
            p = data[0]
            if limit < p:
                return prime + data
            prime.append(p)
            data = [e for e in data if e % p != 0]

    ff = prime_list_eratosthenes(30000)
    from bisect import bisect_left
    q = int(input())
    for _ in range(q):
        n = int(input())
        x = 1 + n
        xx = ff[bisect_left(ff, x)]
        y = xx + n
        yy = ff[bisect_left(ff, y)]
        print(1,x,y,xx*yy)







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
10000"""
        output = """6
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()