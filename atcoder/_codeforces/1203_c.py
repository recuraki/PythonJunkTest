
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    n = int(input())
    dat = list(map(int, input().split()))
    d = {}
    for i in range(n):
        cur = make_divisors(dat[i])
        #print(cur)
        for j in range(len(cur)):
            c = d.get(cur[j], 0)
            d[cur[j]] = c + 1
    res = 0
    for k in d:
        if d[k] == n:
            res += 1

    print(res)


class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """5
1 2 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6
6 90 12 18 30 18"""
        output = """4"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()