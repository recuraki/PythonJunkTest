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
        maze = []
        oh, ow = map(int, input().split())
        for h in range(oh):
            l = list(input())
            maze.append(l)
        #print(maze)
        for w in range(ow):
            canh = oh - 1
            for h in range(oh - 1, -1, -1):
                if maze[h][w] == ".":
                    pass
                elif maze[h][w] == "o":
                    canh = h - 1
                elif maze[h][w] == "*":
                    maze[h][w] = "."
                    maze[canh][w] = "*"
                    canh -= 1
                else:
                    assert False
        for l in maze:
            print("".join(l))



    # n questions
    q = int(input())
    for i in range(q):
        do()
        #if i != (q-1): print()






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
6 10
.*.*....*.
.*.......*
...o....o.
.*.*....*.
..........
.o......o*
2 9
...***ooo
.*o.*o.*o
5 5
*****
*....
*****
....*
*****"""
        output = """..........
...*....*.
.*.o....o.
.*........
.*......**
.o.*....o*

....**ooo
.*o**o.*o

.....
*...*
*****
*****
*****"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()