import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    d = "o" * 15
    s = input()
    s = s + ("o" * (15-len(s)))
    r = 0
    for i in range(len(s)):
        if s[i] == "o":
            r += 1
    print("YES" if r > 7 else "NO")



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
        logging.info("test_input_1")
        input = """oxoxoxoxoxoxox"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """xxxxxxxx"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()