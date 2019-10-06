import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    n %= 12
    l = ((360/12/60) * m) + (30 * n)
    s = (360 / 60) * m
    res = min(abs(l - s), abs(s-l))
    res = 360 - res if res > 180 else res
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
    def test_input1(self):
        print("test_input1")
        input = """15 0"""
        output = """90"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """3 17"""
        output = """3.5"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """6 0"""
        output = """180"""
        self.assertIO(input, output)
    def test_input5(self):
        print("test_input5")
        input = """23 59"""
        output = """5.5000"""
        self.assertIO(input, output)
    def test_input6(self):
        print("test_input5")
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()