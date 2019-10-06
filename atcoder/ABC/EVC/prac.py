import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    q = deque([])
    n = int(input())
    s = input()

    num_open = 0
    num_close = 0

    for i in range(n):
        if s[i] == "(":
            q.appendleft("(")
        elif s[i] == ")":
            if len(q) > 0:
                q.pop()
            else:
                num_close += 1
    num_open = len(q)
    print("(" * num_close + s + ")" * num_open)




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