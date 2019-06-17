import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, t = map(int,input().split())

    dat_a = []
    for i in range(n):
        a = int(input())
        dat_a.append(a)
    dat = []
    dat = [0] * (dat_a[n-1] + t)

    for i in range(n):
        a = dat_a[i]
        dat[a:a + t] = ([1] * t)

    from pprint import pprint
    pprint(sum(dat))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """5 10
20
100
105
217
314"""
        output = """45"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """10 10
1
2
3
4
5
6
7
8
9
10"""
        output = """19"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """10 100000
3
31
314
3141
31415
314159
400000
410000
500000
777777"""
        output = """517253"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()