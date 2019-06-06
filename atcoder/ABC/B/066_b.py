import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    s = s[:-1]
    if len(s) % 2 == 1:
        s = s[:-1]
    for i in range(len(s) // 2):
        f = True
        for j in range(len(s) // 2):
            if s[j] != s[len(s) // 2 + j]:
                f = False
        if f:
            break
        s = s[:-2]

    print(len(s))

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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()