import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    m = []
    f = True
    for i in range(len(s)):
        if s[i] in m:
            f = False
            break
        m.append(s[i])
    print("yes" if f else "no")



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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """different"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()