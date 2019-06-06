import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n  = int(input())
    dat_a = list(map(int, input().split()))

    dat_a = list(map(lambda x: x // 400, dat_a))
    dat_a = list(map(lambda x: 8 if x > 8 else x, dat_a))
    all_color = 0

    for i in range(len(dat_a)):
        if dat_a[i] == 8:
            all_color += 1
    for i in range(all_color):
        dat_a.remove(8)

    dat_a = set(dat_a)

    n_color = len(dat_a)

    mincolor = 0
    maxcolor = 0

    mincolor = n_color
    maxcolor = n_color + all_color
    maxcolor = 8 if maxcolor > 8 else maxcolor
    if mincolor == 0:
        mincolor

    print("{0} {1}".format(mincolor, maxcolor))

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
        logging.info("test_input_1")
        input = """4
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()