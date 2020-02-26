import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = "CODEFESTIVAL2016"
    inp = input()
    c = 0
    for i in range(len(s)):
        if s[i] != inp[i]:
            c += 1
    print(c)

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
        input = """C0DEFESTIVAL2O16"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """FESTIVAL2016CODE"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()