import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def nCr(n, r):
        import math
        # nCrのr>nは組み合わせが存在しないので0を返す
        # raiseすべきのこともあるかも
        if r > n:
            return 0
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

    n = input()
    k = input()
    res = 0

    # 1個下の桁までの合計
    for i in range(k, len(n)):





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
        input = """100
1"""
        output = """19"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """25
2"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """314159
2"""
        output = """937"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3"""
        output = """117879300"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()