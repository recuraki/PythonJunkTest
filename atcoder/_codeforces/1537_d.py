import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors


    def make_divisors_without_own(n):
        r = make_divisors(n)
        if 1 in r: r.remove(1)
        if n in r: r.remove(n)
        return r


    def do():
        n = int(input())
        l = make_divisors_without_own(n)
        print(n, l)

    q = int(input())
    for _ in range(q):
        do()



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
1
4
12
69"""
        output = """Bob
Alice
Alice
Bob"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()