import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    ori = "abcdefghijklmnopqrstuvwxyz"
    s = input()
    for i in range(len(s)):
        ori = ori.replace(s[i], "")
    if len(ori) == 0:
        print("None")
    else:
        print(ori[0])

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
        input = """atcoderregularcontest"""
        output = """b"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """None"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg"""
        output = """d"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()