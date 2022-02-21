import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from decimal import Decimal, ROUND_FLOOR
    s = input()
    n = Decimal(s)
    print( (Decimal(s) / Decimal(10)).quantize(Decimal('0'), rounding=ROUND_FLOOR) )



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
        input = """47"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-24"""
        output = """-3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """50"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """-30"""
        output = """-3"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """987654321987654321"""
        output = """98765432198765432"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()