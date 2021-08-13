import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        def f(n):
            pass
        n = int(input())
        print("---- N = ", n)
        l = []
        for x in list()
    q = int(input())
    for _ in range(q):
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
        input = """5
456
10000
123
314
91"""
        output = """2
4
1
2
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()