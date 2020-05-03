import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = int(input())
    cnt = 0
    val = 100
    import math
    while True:
        cnt += 1
        val = math.floor(float(val) * 1.01)
        if val >= x:
            break
    print(cnt)

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
        input = """103"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()