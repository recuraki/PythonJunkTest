import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    from decimal import Decimal
    from fractions import Fraction
    t, k = map(int, input().split())
    ss = set()
    import math
    for i in range(10000):
        ss.add(math.floor((100 + t) / 100 * i))
    res = []
    buf = []
    cnt = 0
    p = 0
    ans1 = None
    for i in range(10000 - 10):
        if i not in ss:
            cnt += 1
            res.append(i)
            # print(cnt, i, i//34, i - p)
            if k == cnt:
                print(i)
                sys.exit(0)
            buf.append(i - p)
            p = i

    from fractions import Fraction
    import math
    x = (Fraction(k, Fraction(t, 100 + t)))
    x = math.ceil(x) - 1
    moto = int(x / ((100 + t) / 100))
    if int(moto * ((100 + t) / 100)) == x:
        x += 1
    elif int((moto + 1) * ((100 + t) / 100)) == x:
        x += 1
    print(x)

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
        input = """10 1"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5"""
        output = """171"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1000000000"""
        output = """100999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()