import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat = set()
    all_color = 0

    for i in range(n):
        if dat_a[i] < 400:
            dat.add("a")
        elif dat_a[i] < 800:
            dat.add("b")
        elif dat_a[i] < 1200:
            dat.add("c")
        elif dat_a[i] < 1600:
            dat.add("d")
        elif dat_a[i] < 2000:
            dat.add("e")
        elif dat_a[i] < 2400:
            dat.add("f")
        elif dat_a[i] < 2800:
            dat.add("g")
        elif dat_a[i] < 3200:
            dat.add("h")
        else:
            all_color += 1

    colored = len(dat)

    resmin = colored
    if resmin == 0 and all_color > 0:
        resmin = 1

    resmax = colored + all_color
    #if resmax > 8:
    #    resmax = 8

    print("{0} {1}".format(str(resmin), str(resmax)))



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
        input = """10
1 3400 3400 3400 3400 3400 3400 3400 3400 3400"""
        output = """1 8"""
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