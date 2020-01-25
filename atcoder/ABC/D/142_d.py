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
        # divisors.sort()
        return divisors

    a, b = map(int, input().split())
    aa = set(make_divisors(a))
    bb = set(make_divisors(b))
    u = aa & bb
    u = u - set([1])
    #print(u)
    u = list(u)
    import itertools
    res = 0

    def each_prime(l):
        f = True
        import fractions
        for i in range(len(l)):
            for j in range(1, len(l) - i):
                if fractions.gcd(l[i], l[i + j]) != 1:
                    f = False
                    break
            if f is False:
                break
        return f

    for i in range(1, len(u)):
        for l in itertools.combinations(u, i):
            print("try: {0}".format(l))
            l = list(l)
            if each_prime(l):
                res = i
                break

    print(res + 1)



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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()