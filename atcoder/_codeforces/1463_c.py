import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
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
        input = """8
3
1 5
3 0
6 4
3
1 5
2 4
10 -5
5
2 -5
3 1
4 1
5 1
6 1
4
3 3
5 -3
9 2
12 0
8
1 1
2 -6
7 2
8 3
12 -9
14 2
18 -1
23 9
5
1 -4
4 -7
6 -1
7 -3
8 -7
2
1 2
2 -2
6
3 10
5 5
8 0
12 -4
14 -7
19 -5"""
        output = """1
2
0
2
1
1
0
2"""
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