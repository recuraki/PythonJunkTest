import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        def dodo(x, shinsu):
            res = 0
            ll = len(x)
            for i in range(len(x)):
                res += int(x[i]) * (shinsu ** (ll - 1 - i))
            return res
        s = input()
        m = int(input())
        l = 0
        for i in range(len(s)):
            l = max(l, int(s[i]))
        l += 1
        minl = l
        h = 10 ** 18 * 10
        while l <= h:
            mid = (l + h) // 2
            if dodo(s, mid) <= m:
                l = mid + 1
            else:
                h = mid - 1
        if mid == 10000000000000000000:
            print(1)
            return
        for i in range(5, -5, -1):
            if mid < 1:
                continue
            if dodo(s, mid + i) <= m:
                res = mid + i
                #print("res", res)
                print(max(res - minl + 1, 0) )
                return
        print(0)
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
        input = """22
10"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """999
1500"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000000000000000000000000000000000000000000000000000000000
1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """22
8"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """1
1"""
        output = """0"""
        self.assertIO(input, output)


    def test_input_6(self):
        print("test_input_6")
        input = """1
100"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()