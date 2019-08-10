
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    while True:
        a = str(n)
        a = list(map(int, a))
        a = sum(a)
        if a % 4 == 0:
            break
        n += 1

    print(n)

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
        input = """432"""
        output = """435"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """99"""
        output = """103"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """237"""
        output = """237"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """42"""
        output = """44"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()