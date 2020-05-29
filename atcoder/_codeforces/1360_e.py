import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    for _ in range(q):
        #print("---")
        goal = []
        maze = []
        n = int(input())
        for i in range(n):
            l = [0] * n
            maze.append(l)
            l = list(map(int, input()))
            goal.append(l)
        #pprint(maze)
        #print(goal)
        for turn in range(n, 0, -1):
            targets = []
            #print("turn", turn)
            for i in range(turn-1):
                targets.append( [turn-1, i] )
                targets.append( [i, turn-1] )
            targets.append([turn - 1, turn - 1])
            #print(targets)

            isChange = True
            while isChange is True:
                isChange = False
                for yy, xx in targets:
                    if goal[yy][xx] == 0:
                        continue
                    if maze[yy][xx] == 1:
                        continue
                    # goal = 1 but maze = 0
                    nyy, nxx = yy + 1, xx + 1
                    if nxx >= n or nyy >= n: # can block
                        maze[yy][xx] = 1
                        isChange = True
                        continue
                    #print(nyy, nxx, "!!!")
                    if maze[nyy][xx] == 1 or maze[yy][nxx] == 1:
                        maze[yy][xx] = 1
                        isChange = True
                        continue

            #pprint(maze)
        #print("Final")
        if maze == goal:
            print("YES")
        else:
            print("NO")
        #print(maze)
        #print(goal)


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
4
0010
0011
0000
0000
2
10
01
2
00
00
4
0101
1111
0101
0111
4
0100
1110
0101
0111"""
        output = """YES
NO
YES
YES
NO"""
        self.assertIO(input, output)


    def test_input_2(self):
        print("test_input_2")
        input = """1
1
1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_2")
        input = """1
1
0"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()