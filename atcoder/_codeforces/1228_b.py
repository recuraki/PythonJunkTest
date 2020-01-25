import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 1000000007
    a, b = map(int, input().split())
    dat = []
    for i in range(a):
        dat.append([0] * b)
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))

    can = True

    for i in range(a):
        for j in range(aa[i]):
            dat[i][j] = 1
        if aa[i] != b:
            dat[i][aa[i]] = 2



    for i in range(b):
        for j in range(bb[i]):
            if dat[j][i] == 2:
                can = False
            dat[j][i] = 1
        if bb[i] != a:
            if dat[bb[i]][i] == 1:
                #print("f3")
                can = False
            dat[bb[i]][i] = 2

    res = 1
    import collections
    for i in range(a):
        #print(dat[i])
        c = collections.Counter(dat[i])
        if 0 not in c:
            x = 0
        else:
            x = c[0]
        res *= (2 ** x)
        res %= mod


    if can is False:
        print(0)
    else:
        print(res)



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
        input = """3 4
0 3 1
0 2 3 0"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
1
0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """19 16
16 16 16 16 15 15 0 5 0 4 9 9 1 4 4 0 8 16 12
6 12 19 15 8 6 19 19 14 6 9 16 10 11 15 4"""
        output = """797922655"""
        self.assertIO(input, output)



    def test_input_22(self):
        print("test_input_22")
        input = """1 1
0
0"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_222(self):
        print("test_input_222")
        input = """2 2
0 1
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()