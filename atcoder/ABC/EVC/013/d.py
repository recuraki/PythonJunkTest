import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    num_overopen = 0
    num_overclose = 0
    import collections
    q = collections.deque([])
    for i in range(n):
        if s[i] == "(":
            q.append("(")
        if s[i] == ")":
            if len(q) == 0:
                num_overclose += 1
            else:
                q.pop()
    print( ("(" * num_overclose) + s + (")" * len(q)))



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
())"""
        output = """(())"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """6
)))())"""
        output = """(((()))())"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """8
))))(((("""
        output = """(((())))(((())))"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()