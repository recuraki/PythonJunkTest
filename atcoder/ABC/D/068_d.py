import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k = int(input())
    if k == 0:
        print(4)
        print("3 3 3 3")
    elif k < 51:
        print(50)
        d = (["50"] * (k))
        d = d  + (["0"] * (50 - k))
        #print(d)
        print(" ".join(d))
    else:
        import math
        k -= 50
        kkm = k % 50
        d = [ str(50 + math.floor(k // 50)) ] * 50
        for i in range(kkm):

        for i in range(kkm):
            d[i] = str(int(d[i])+ 1 )
        print(50)
        print(" ".join(d))


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
        input = """51"""
        output = """4
3 3 3 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """3
1 0 3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2"""
        output = """2
2 2"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """3"""
        output = """7
27 0 0 0 0 0 0"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """1234567894848"""
        output = """10
1000 193 256 777 0 1 1192 1234567891011 48 425"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()