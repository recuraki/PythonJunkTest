import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    def do():
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))
        if x >= total:
            print("Yes")
        else:
            print("No")

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
        input = """2 3
1 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 10
3 3 4 4"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 30
3 1 4 1 5 9 2 6"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()