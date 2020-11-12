import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        if n == 1:
            print(2)
            return
        res = []
        for i in range(4*n - (2*(n-1)), 4*n+1, 2):
            res.append(i)
        print(" ".join(list(map(str, res))))

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
        input = """3
2
3
4"""
        output = """6 4
4 6 10
14 10 12 8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()