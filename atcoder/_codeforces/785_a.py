import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m, k = map(int, input().split())
    dat = list(map(int, input().split()))
    minis = []
    for i in range(n // m + 1):
        for ii in range(m):
            minis.append(-k * (i+1))

    total = sum(dat)
    t_from_l = [0] * n
    t_from_r = [0] * n
    t_from_l[0] = dat[0]

    t_from_r[n-1] = dat[-1]

    for i in range(1, n):
        t_from_l[i] += t_from_l[i-1] + dat[i]
    for i in range(n-1, 0, -1):
        t_from_r[i-1] += t_from_r[i] + dat[i-1]
    print(total)

    print(t_from_l)
    print(t_from_r)
    m = 0
    for l in range(n):
        j = 0
        for r in range(l, n):
            print(total - t_from_l[l] - t_from_r[r] + minis[j])
            m = max(m, total - t_from_l[l] - t_from_r[r] + minis[j])
            j += 1
    print(m)








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
        input = """7 3 10
2 -4 15 -3 4 8 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """5 2 1000
-13 -4 -9 -20 -11"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()