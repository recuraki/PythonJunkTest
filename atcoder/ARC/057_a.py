import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    t = 2 * 10**12
    a, k = map(int, input().split())
    if k == 0:
        print(t - a)
    else:
        d = 0
        while True:
            a += 1 + k * a
            if a >= t:
                print(d+1)
                break
            d += 1

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
        input = """1000 300"""
        output = """4"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """6 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """567876543 0"""
        output = """1999432123457"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()