import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dat = list(map(lambda x: int(x) % m, input().split()))
    dat.sort(reverse=False)
    l, r = 0, 1
    res = dat[0]
    print(dat)
    final = -1
    while l < n and r < n:
        if m > (res + dat[r]):
            res += dat[r]

            final = max(final, res)
            r += 1
        else:
            res -= dat[l]
            final = max(final, res)
            l += 1
    print(final)



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
        input = """4 3
1 2 3 4
"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 4
4 8
"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """50 1974806404
1473144501 1739000682 1498617648 669908539 1387036160 12895152 1144522536 1812282135 1328104340 1380171693 1113502216 860516128 777720505 1543755630 1722060050 1455590965 328298286 70636430 136495344 1472576336 402903178 1329202901 1503885239 1219407972 2416950 12260290 655495368 561717989 1407392293 1841585796 389040744 733053145 1433102830 1887658391 1402961683 672655341 1900553542 400000570 337453827 1081174233 1780172262 1450956043 1941690361 410409118 847228024 1516266762 1866000082 1175526310 1586903191 2002495426
"""
        output = """1974018344"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()