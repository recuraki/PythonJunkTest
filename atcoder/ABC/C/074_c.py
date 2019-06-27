import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c,d,e,f = map(int, input().split())

    ma_per = -1
    ma_w = -1
    ma_s = -1

    for aa in range(31):
        for bb in range(31):
            for cc in range(101):
                for dd in range(101):
                    w = 100 * aa * a + 100 * bb * b
                    s = cc * c + dd * d
                    if (w + s) > f:
                        break
                    if s > (w * e / 100):
                        break
                    if w+s == 0:
                        break
                    per = 100 * s / (w + s)
                    if per > ma_per:
                        ma_per = per
                        ma_w = w
                        ma_s = s

    print("{0} {1}".format(ma_w + ma_s, ma_s))



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
        input = """1 2 10 20 15 200"""
        output = """110 10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2 1 2 100 1000"""
        output = """200 100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """17 19 22 26 55 2802"""
        output = """2634 934"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()