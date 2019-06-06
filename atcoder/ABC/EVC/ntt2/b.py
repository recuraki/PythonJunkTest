import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    d = {}
    n = int(input())
    for i in range(n):
        s = input()
        c = d.get(s, 0)
        d[s] = c + 1
    m = int(input())
    for i in range(m):
        s = input()
        c = d.get(s, 0)
        d[s] = c - 1
    co = 0
    wo = ""
    for k in d:
        if d[k] > co:
            co = d[k]
            wo = k
    print(co if co > 0 else "0")




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
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3
apple
orange
apple
5
apple
apple
apple
apple
apple"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()