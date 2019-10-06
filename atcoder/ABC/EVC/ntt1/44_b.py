import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    w = input()
    d = dict()
    for i in range(len(w)):
        c = w[i]
        count = d.get(c, 0)
        d[c] = count + 1
    f = True
    for k in d:
        if d[k] % 2 != 0:
            f = False
    print("Yes" if f else "No")


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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()