import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    """
    Wを右に寄せる行為に他ならない
    :return:
    """
    s = input()
    dat = []
    wcount = 0
    res = 0
    for i in range(len(s)):
        if s[i] == "W":
            res += (i - wcount)
            wcount += 1
            dat.append(i)
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
        input = """BBW"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """BWBWBW"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()