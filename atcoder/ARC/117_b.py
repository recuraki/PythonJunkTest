import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    m = 10**9 + 7
    def f(a, b): #　2つの隣接するa,bがあった際(a>b)の組み合わせ数
        return (a - b + 1) * (b + 1)
    def do():
        res = 1
        n = int(input())
        dat = list(map(int, input().split()))
        dat.append(0)
        dat = list(set(dat))
        dat.sort(reverse=True)
        for i in range(len(dat) - 1):
            x, y = dat[i], dat[i+1]
            res *= f(x-y, 0)
            res %= m
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
        input = """2
1 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
5 3 4 1 5 2"""
        output = """32"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
314 159 265 358 979 323 846"""
        output = """492018656"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()