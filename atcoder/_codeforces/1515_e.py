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



    import sys
    read = sys.stdin.read
    n, *indata = map(int, read().split())
    dat = []
    offset = 0




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
        input = """3 100000007"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 100000007"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """400 234567899"""
        output = """20914007"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()