import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k = int(input())
    s = input()
    l = len(s)
    if l <= k:
        print(s)
    else:
        print(s[:k] + "...")

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
        input = """7
nikoandsolstice"""
        output = """nikoand..."""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """40
ferelibenterhominesidquodvoluntcredunt"""
        output = """ferelibenterhominesidquodvoluntcredunt"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()