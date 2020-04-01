import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, c, k = map(int, input().split())
    dat = []
    for _ in range(n):
        dat.append(int(input()))
    dat.sort()
    cn = 1
    nt = dat[0] + k
    res = 1
    for i in range(1, n):
        #print("i", i, "res", res)
        # もう前のバスがいっぱい
        if cn == c:
            #print("full")
            cn = 1
            nt = dat[i] + k
            res += 1
            continue
        if dat[i] > nt:
            #print("gogogo")
            cn = 1
            nt = dat[i] + k
            res += 1
            continue
        cn += 1
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
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()