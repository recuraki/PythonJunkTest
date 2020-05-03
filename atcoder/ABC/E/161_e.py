import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k, c = map(int, input().split())
    s = input()
    dat = []
    for i in range(n):
        if s[i] == "o":
            dat.append(i+1)
    print(dat)
    if n == 1:
        print(1)
    else:
        res = []
        last = -100
        restuntil = -100
        for i in range(0, len(dat)):
            d = dat[i] - last
            if d > c:
                res.append(dat[i])
            else:
                del res[-1]
            last = dat[i]
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
        input = """11 3 2
ooxxxoxxxoo"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2 3
ooxoo"""
        output = """1
5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 1 0
ooooo"""
        output = """"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """16 4 3
ooxxoxoxxxoxoxxo"""
        output = """11
16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()