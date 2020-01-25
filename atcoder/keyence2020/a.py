import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h = int(input())
    w = int(input())
    n = int(input())
    a = b = 100000000
    for i in range(h+1):
        if n <= i * w:
            a = i
            break
    for i in range(w+1):
        if n <= i * h:
            b = i
            break
    print(min(a,b))

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
        input = """3
7
10"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """14
12
112"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
100
200"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()