import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    a,b,c = 0,0,0
    for i in range(len(s)):
        if s[i] == "a":
            a+=1
        if s[i] == "b":
            b+=1
        if s[i] == "c":
            c+=1
    if max(a,b,c) == a:
        print("a")
    if max(a,b,c) == b:
        print("b")
    if max(a,b,c) == c:
        print("c")

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
        input = """abbc"""
        output = """b"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """cacca"""
        output = """c"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """b"""
        output = """b"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """babababacaca"""
        output = """a"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()