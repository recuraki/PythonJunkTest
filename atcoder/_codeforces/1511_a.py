import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = dat.count(1) + dat.count(3)
        print(res)


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
        input = """4
1
2
3
1 2 3
5
1 1 1 1 1
3
3 3 2"""
        output = """0
2
5
2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()