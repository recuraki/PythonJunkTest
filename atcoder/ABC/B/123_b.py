import sys
from io import StringIO
import unittest

def resolve():
    import math
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    dat = [a,b,c,d,e]
    dattime = map
    tindex = 0
    tnum = 10

    for i in range(5):
        t = dat[i] % 10
        t = 10 if t == 0 else t
        if tnum > t:
            tindex = i
            tnum = t

    sum = 0

    for i in range(5):
        if i != tindex:
            sum += int( math.ceil(dat[i] / 10) * 10 )
        else:
            sum += dat[i]
    print(sum)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
10
10
10
10"""
        output = """50"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()



