import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = list(input())
    count = 0
    for i in range(n - 1):
        if s[i] == ".":
            continue
        if s[i + 1] == ".":
            s[i] = "."
            count += 1
    print(count)



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
        logging.info("test_input_1")
        input = """3
#.#"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """5
#.##."""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """9
........."""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()