import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        s = input()
        n = int(input())
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))


    # 1 time
    do()
    # n questions
    q = int(input())
    for _ in range(q):
        do()






    # list output [1,2,3] -> 1 2 3
    dat = [1, 2, 3]
    print(" ".join(list(map(str, dat))))

    pass
    #sys.setrecursionlimit(100000)

    # very fast read
    import sys
    read = sys.stdin.read
    n, *indata = map(int, read().split())
    dat = []
    offset = 0
    # pat1
    a, b, c = dat[offset:offset+3]
    offset += 3
    # pat2
    querytype = dat[offset]
    offset += 1
    if querytype == 1:
        a, b, c = dat[offset:offset + 3]
        offset += 3
    elif querytype == 2:
        a, b = dat[offset:offset + 2]
        offset += 2

    # for maze
    dh = [-1, 0, 0, 1]
    dw = [0, -1, 1, 0]
    maze = []
    oh , ow = 0,0
    for h in range(oh):
        l = list(input().split())
        maze.append(l)

    # maze wall
    maze = []
    oh , ow = 3,3
    maze.append(["#"] * (ow + 2))
    for h in range(oh):
        l = ["#"] + list(input()) + ["#"]
        maze.append(l)
    maze.append(["#"] * (ow + 2))
    print(maze)






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
        self.assertIO(input
                      , output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()