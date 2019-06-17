import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    o = input()
    e = input()
    for i in range(len(o)):
        print(o[i], end="")
        if i < len(e):
            print(e[i], end="")
    print("")

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
        input = """xyz
abc"""
        output = """xaybzc"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """atcoderbeginnercontest
atcoderregularcontest"""
        output = """aattccooddeerrbreeggiunlnaerrccoonntteesstt"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()