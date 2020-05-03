import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 998244353
    n = int(input())
    import collections
    dat = list(map(int, input().split()))
    c = collections.Counter(dat)
    ma = max(c)
    #print(c)
    res = 1
    #print(c)
    can = True

    for i in range(1,ma ):
        #print("{0} ^ {1}".format(i, i+1))
        #print("={0} ^ {1}".format(c[i], c[i+1]))
        #res *= c[i] ** (c[i+1])
        if c[i] == 0:
            can = False
            break
        for ii in range(c[i+1]):
            res *= c[i]
            res %= mod
            #print("=={0}".format(res))


    if dat[0] != 0:
        print(0)
    elif c[0] != 1:
        print(0)
    elif can is False:
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
        input = """4
0 1 1 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
0 3 2 1 2 2 1"""
        output = """24"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """7
0 4 3 2 3 3 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_32(self):
        print("test_input_31")
        input = """7
0 3 2 1 2 2 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()