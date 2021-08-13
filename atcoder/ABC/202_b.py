import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    d = dict()
    d["0"] = "0"
    d["1"] = "1"
    d["8"] = "8"
    d["6"] = "9"
    d["9"] = "6"
    s = input()
    res = ""
    s = list(s)
    s.reverse()
    for x in s:
        res += d[x]
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
        input = """0601889"""
        output = """6881090"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """86910"""
        output = """01698"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """01010"""
        output = """01010"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()