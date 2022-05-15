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




    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        oh, ow = map(int, input().split())

        maze = []
        maze.append(["#"] * (ow + 2))
        for h in range(oh):
            l = ["#"] + list(input()) + ["#"]
            maze.append(l)
        maze.append(["#"] * (ow + 2))
        #print(maze)

        for h in range(1, oh + 2):
            for w in range(1, ow + 2):
                if maze[h][w] == "#": continue
                if maze[h][w] == "0": continue # SKIP
                if maze[h][w] == "2": continue # SKIP
                # rec!
                # detect size
                sizew = 0
                i = w
                while maze[h][i] == "1":
                    sizew += 1
                    i += 1
                sizeh = 0
                i = h
                while maze[i][w] == "1":
                    sizeh += 1
                    i += 1
                # this rect must be sizeh x sizew
                for hh in range(h, h+sizeh):
                    for ww in range(w, w+sizew):
                        if maze[hh][ww] == "0":
                            print("NO")
                            return
                        maze[hh][ww] = "2"

                # edge?
                for hh in range(h, h+sizeh):
                    if maze[hh][w + sizew] in ["1", "2"]:
                        print("NO")
                        return
                for ww in range(w, w+sizew):
                    if maze[h + sizeh][ww] in ["1", "2"]:
                        print("NO")
                        return
        print("YES")

    # n questions
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
3 3
100
011
011
3 3
110
111
110
1 5
01111
4 5
11111
01010
01000
01000
3 2
11
00
11"""
        output = """YES
NO
YES
NO
YES"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """5
1 1
1
1 1
0
2 2
11
11
2 2
10
01
3 3
111
111
111
"""
        output = """YES
YES
YES
YES
YES"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """5
3 3
111
101
111
3 3
111
110
111
3 3
011
111
111
3 3
011
101
111
3 3
111
011
111
"""
        output = """NO
NO
NO
NO
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()