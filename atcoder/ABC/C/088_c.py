import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    dat = []
    for _ in range(3):
        dat.append(list(map(int, input().split())))
    f = True
    a1,a2,a3,b1,b2,b3 = -1,-1,-1,-1,-1,-1
    a1 = 0
    b1 = dat[0][0]
    b2 = dat[0][1]
    b3 = dat[0][2]

    a2 = dat[1][0] - b1
    a3 = dat[2][0] - b1

    if dat[1][1] != a2 + b2:
        f = False

    if dat[1][2] != a2 + b3:
        f = False

    if dat[2][1] != a3 + b2:
        f = False

    if dat[2][2] != a3 + b3:
        f = False

    #if 0 > a1 or 0>a2 or 0>a3 or 0>b1 or 0>b2 or 0>b3:
    #    f = False

    #print(a1,a2,a3,b1,b2,b3)
    print("Yes" if f else "No")



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
        input = """1 0 1
2 1 2
1 0 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2 2
2 1 2
2 2 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 8 8
0 8 8
0 8 8"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1 8 6
2 9 7
0 7 7"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()