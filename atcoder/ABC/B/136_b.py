import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = 0
    for i in range(1,  n + 1):
        if len(str(i)) % 2 == 1:
            res += 1
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
        input = """11"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """136"""
        output = """46"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000"""
        output = """90909"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()