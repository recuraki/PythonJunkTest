import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    a, b = map(int, input().split())
    res = None
    for i in range(1, 200000):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            res = i
            break
    if res is not None:
        print(res)
    else:
        print(-1)




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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()