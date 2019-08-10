import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = ""
    l = []
    for i in range(n):
        if i %2 == 0:
            l.append("I hate ")
        else:
            l.append("I love ")
    s += "that ".join(l) + "it"
    print(s)

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
        input = """1"""
        output = """I hate it"""
        self.assertIO(input, output)


    def test_input_12(self):
        print("test_input_12")
        input = """2"""
        output = """I hate that I love it"""
        self.assertIO(input, output)

    def test_input_132(self):
        print("test_input_123")
        input = """3"""
        output = """I hate that I love that I hate it"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()