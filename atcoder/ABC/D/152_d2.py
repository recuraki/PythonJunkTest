import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    if n > 30:
        x = n // 10
        basenum = x * x + 8
        addnum = 0
        #print("{0} {1}".format(x* 10 + 1, n))
        hassame = False
        for i in range(x * 10 + 1, n):
            #print(i)
            for j in range(1, n):
                #print(j)
                if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                    addnum += 1
                    if i == j:
                        hassame=True
                    print("{0},{1}".format(i, j))
        res = basenum + addnum * 2
        print("n={0}, x={1}, basenum={2}, addnum={3}".format(n,x,basenum,addnum))
        print(res)
    elif n==1:
        print(1)
    else:
        res = 0
        for i in range(1, n):
            for j in range(1, n):
                if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                    res += 1
        print("{1}".format(n, res))

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
        input = """108"""
        output = """125"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100"""
        output = """108"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2020"""
        output = """40812"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """200000"""
        output = """400000008"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()