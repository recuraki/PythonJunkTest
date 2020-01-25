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
    for ds in divs:
        t = 0
        for i in range(n):
            #t += (dat[i] % ds)
            t += min( (dat[i] % ds) , abs((dat[i] % ds) - ds))
            #print(" = {0} ... {1}".format(dat[i], min( (dat[i] % ds) , abs((dat[i] % ds) - ds))))
        #print("end: {0} {1}".format(ds, t))
        if t < (k * 2):
            res = ds
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