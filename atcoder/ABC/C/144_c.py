import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 約数のリストを表示する(因数分解ではない)
    # make_divisors(16)
    # [1, 16, 2, 8, 4]
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors

    # 約数のリストを表示する(1とその数を除く)
    # make_divisors_without_own(16)
    # [2, 8, 4]
    def make_divisors_without_own(n):
        r = make_divisors(n)
        r.remove(1)
        r.remove(n)
        return r
    n = int(input())

    r = make_divisors_without_own(n)
    r.sort()
    if len(r) == 0:
        print(n - 1)
    else:
        a = r[len(r) // 2]
        b = n // a
        print(a - 1 + b - 1)



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
        input = """10"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """50"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10000000019"""
        output = """10000000018"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()