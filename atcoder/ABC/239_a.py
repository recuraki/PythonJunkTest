import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import math
    n = int(input())
    x = math.sqrt( n*(12800000 + n) )
    print(x)

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
        input = """333"""
        output = """65287.907678222"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """634"""
        output = """90086.635834623"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()