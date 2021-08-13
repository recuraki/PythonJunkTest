import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    def do():
        import math
        from decimal import Decimal
        r, x, y = map(int, input().split())
        r = Decimal(r)
        x = Decimal(x)
        y = Decimal(y)
        r = r * r
        target = x ** 2 + y ** 2
        res = math.ceil((target / r).sqrt())
        for i in range(res-3, res+3):
            if i < 0:
                continue
            #print(i, r*i, target)
            if r * i**2 >= target:
                res = i
                break
        if res == 1:
            if r * i**2 != target:
                res += 1
        print(res)

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
        input = """5 15 0"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 11 0"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 4 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100 0 100"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()