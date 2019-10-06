import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    if s.find("W") == -1 or s.find("B") == -1:
        print(0)
    elif len(s) == 1:
        print(2)
    else:
        res = 0
        c = s[0]
        for i in range(len(s) - 1):
            if c != s[1+i]:
                c = s[1+i]
                res += 1
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
        input = """BBBWW"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """WWWWWW"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """WBWBWBWBWB"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()