import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h1, w1 = map(int, input().split())
    h2, w2 = map(int, input().split())
    l = [h2, w2]
    if h1 in l or w1 in l:
        print("YES")
    else:
        print("NO")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """1080 1920
1080 1920"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1080 1920
1920 1080"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """334 668
668 1002"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """100 200
300 150"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input5(self):
        print("test_input5")
        input = """120 120
240 240"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()