import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat_aa = map(lambda x: x*2, dat_a)
    dat_aa = list(dat_aa)
    s_in = sum(dat_a)

    m = -1
    index = -1
    for i in range(n):
        if dat_aa[i] > m:
            m = dat_aa[i]
            index = i
    res = [0] *n

    for i in range(n):
        if i > 0:
            res[i] = dat_aa[i-1] - res[i-1]
        else:
            res[i] = dat_aa[n-1] - res[i]
    s_out = sum(res)
    d = s_in - s_out

    for i in range(n):
        if i % 2 == 0:
            res[i] += d
        else:
            res[i] -= d
    res = list(map(str, res))
    print(" ".join(res))



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
        input = """3
2 2 4"""
        output = """4 0 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 8 7 5 5"""
        output = """2 4 12 2 8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1000000000 1000000000 0"""
        output = """0 2000000000 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()