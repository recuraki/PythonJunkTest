import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        dat = []
        for i in range(n-1):
            dat.append(i+2)
        dat.append(1)

        print(" ".join(list(map(str, dat))))

    q = int(input())
    for qq in range(q):
        do()



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
        input = """2
2
5"""
        output = """xxx"""
        self.assertIO(input, output)