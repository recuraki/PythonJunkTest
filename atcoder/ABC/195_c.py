import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    res = 0
    print(s)
    for i in range (0,len(s) - 1):
        numcomma = (len(s) - 1 - i) // 3 # その桁で何個コンマ？
        x = int(s[i]) # その桁の数
        print("i ",i, x, res, numcomma)
        # まず、明らかに大きい数を計算
        a = 0
        y = 0
        zeronum = len(s) - 1 - i
        if x == 0:
            a = numcomma * 9 * ( (10**zeronum) )
            res += a
        else:
            a = ( (x-1) * (10**(zeronum+0)) )
            t = s[i+1:]
            y = (int(t) + 1)
            res += (a+y) * numcomma
        print(" > after:", res, a, y,a+y )
        pass
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
        input = """1010"""
        output = """11"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """27182818284590"""
        output = """107730272137364"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2000"""
        output = """1001"""
        self.assertIO(input, output)
    def test_input_311(self):
        print("test_input_311")
        input = """2001"""
        output = """1002"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """10000"""
        output = """9001"""
        self.assertIO(input, output)
    def test_input_32(self):
        print("test_input_32")
        input = """20432"""
        output = str(9000+10000+433)
        self.assertIO(input, output)
    def test_input_322(self):
        print("test_input_322")
        input = """10321"""
        output = str(9000+10000+433)
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()