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
    def do():
        from decimal import Decimal
        n, k, x = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()

        cur = []
        groups = 0
        resgroup = []
        diffs = []
        prev = dat[0]
        for nextval in dat:
            if (nextval - prev) > x:
                resgroup.append(cur)
                diffs.append(nextval - prev)
                cur = []
                groups += 1
            cur.append(nextval)
            prev = nextval
        resgroup.append(cur)
        cur = []
        groups += 1
        import math
        def f(diffs):
            ceil = lambda  a, b: ((a) + ((b) - 1)) // (b)
            assert diffs > x
            diffs -= x
            #print(diffs, x)
            print(math.ceil((Decimal(diffs) / Decimal(x))), ceil(diffs, x))
            return math.ceil((Decimal(diffs) / Decimal(x)))

        #print(diffs)
        diffs.sort()
        res = groups
        for diffval in diffs:
            needk = f(diffval)
            if k < needk:
                break
            k -= needk
            res -= 1

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
        input = """8 2 3
1 1 5 8 12 13 20 22"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """13 0 37
20 20 80 70 70 70 420 5 1 5 1 60 90"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """8 499999999999999999 2
1000000000000000000 1 1 1000000000000000000 1 1 1000000000000000000 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_22(self):
        print("test_input_22")
        input = """5 49 2
100 1 1 100 1 1 100 1"""
        output = """1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()