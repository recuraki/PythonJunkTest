import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a = int(input())
    b = (180 - a) // 2
    print(180 - b)




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
        input = """60"""
        output = """120"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """30"""
        output = """105"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """90"""
        output = """135"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()