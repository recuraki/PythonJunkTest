import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    mod = 10**9 + 7
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = 1
        dat.sort()
        for i in range(n):
            x = dat[i]
            if x - i <= 0:
                print(0)
                return
            res *= max(0, x - i)
            res %= mod
        print(res % mod)
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
        input = """2
1 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
3 3 4 4"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10
999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979"""
        output = """405924645"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()