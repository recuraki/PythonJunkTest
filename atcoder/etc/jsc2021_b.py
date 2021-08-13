import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n, m = map(int, input().split())
        data = set(map(int, input().split()))
        datb = set(map(int, input().split()))
        res = []
        for i in range(1, 2000):
            if i in data and i not in datb:
                res.append(i)
                continue
            if i not in data and i in datb:
                res.append(i)
                continue
        print(" ".join(list(map(str, res))))

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
        input = """2 2
1 2
1 3"""
        output = """2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 4
1 2 3 4
1 2 3 4"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()