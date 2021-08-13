import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        from math import log
        a, b, c = map(int, input().split())
        if log(a)+log(c) > log(b)+log(c):
            print(">")
            return
        if log(a)+log(c) < log(b)+log(c):
            print("<")
            return
        if log(a)+log(c) == log(b)+log(c):
            print("=")
            return
    do()



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
        input = """3 2 4"""
        output = """>"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-7 7 2"""
        output = """="""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """-8 6 3"""
        output = """<"""
        self.assertIO(input, output)
    def test_input_13(self):
        print("test_input_13")
        input = """-2 2 4"""
        output = """="""
        self.assertIO(input, output)
    def test_input_113(self):
        print("test_input_113")
        input = """-2 2 3"""
        output = """<"""
        self.assertIO(input, output)
    def test_input_1113(self):
        print("test_input_1113")
        input = """2 2 3"""
        output = """="""
        self.assertIO(input, output)
    def test_input_1113(self):
        print("test_input_1113")
        input = """2 2 4"""
        output = """="""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()