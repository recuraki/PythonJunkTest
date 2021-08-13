import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        s = input()
        n = int(input())
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))

    q = int(input())
    for _ in range(q):
        do()
    # do()


    dat = [1, 2, 3]
    print(" ".join(list(map(str, res))))

    pass
    #sys.setrecursionlimit(100000)
    import math
    math.ceil(1.2)
    math.floor(1.2)
    round(1.2, 3)

    maze = []
    h, w = 0, 0
    for hh in range(h):
        l = list(map(int, input().split()))
        #l = list(input())
        maze.append(l)





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
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()