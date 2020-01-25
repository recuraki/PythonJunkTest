import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    is_ac = [False] * 200050
    count_wa = [0] * 100050
    numok = 0
    numwa = 0
    for i in range(m):
        p, s = input().split()
        p = int(p)
        if is_ac[p]: # すでに正解
            continue
        else: # 未正解
            if s == "AC":
                numok += 1
                is_ac[p] = True
            else:
                count_wa[p] += 1
    for i in range(100040):
        if is_ac[i]:
            numwa += count_wa[i]
    print("{0} {1}".format(numok, numwa))



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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()