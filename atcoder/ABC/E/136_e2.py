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
        divisors.sort()
        divisors.reverse()
        return divisors

    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    dat = list(map(abs, dat))
    total = sum(dat)
    divs = make_divisors(total)
    #print()
    for ds in divs:
        a1 = 0 # 引くほう
        a2 = 0 # 足すほう
        for i in range(n):
            if (dat[i] % ds) <  abs((dat[i] % ds) - ds):
                a1 += dat[i] % ds
            else:
                a2 += abs((dat[i] % ds) - ds)
            #print(" = {0} ... a1{1} a2".format(dat[i], a1, a2))
        d = abs(a2-a1)
        print("end: {0} a1 {1} a2 {2} diff{3}".format(ds, a1, a2, abs(a2-a1)))
        if d <= k and a1 <= k and a2 <= k:
            break
    print(ds)


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
        input = """2 3
8 20"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 10
3 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 5
10 1 2 22"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8 7
1 7 5 6 8 2 6 5"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()