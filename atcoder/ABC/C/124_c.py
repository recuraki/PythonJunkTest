import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    res_s0 = 0
    res_s1 = 0

    #print("s0")
    for i in range(len(s)):
        #print(i, end="")
        if i % 2 == 0:
            if s[i] != "0":
                res_s0 += 1
                #rint("!")
        else:
            if s[i] != "1":
                res_s0 += 1
                #print("!")

    #print()
    #print("s1")

    for i in range(len(s)):
        #print(i, end="")
        if i % 2 == 0:
            if s[i] != "1":
                res_s1 += 1
                #print("!")
        else:
            if s[i] != "0":
                res_s1 += 1
                #print("!")

    #print("---")
    #print(res_s0)
    #print(res_s1)
    print(min(res_s0, res_s1))
"""
10010010
10101010
  xxx

10010010
01010101
xx   xxx
"""


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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()