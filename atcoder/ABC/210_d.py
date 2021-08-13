import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint

    def do():
        oh, ow, c = map(int, input().split())
        maze = []
        for _ in range(oh):
            l = list(map(int, input().split()))
            maze.append(l)
        res = 10 ** 18

        cost = [[10**18] * ow for _ in range(oh)]
        cost[0][0] = maze[0][0]
        for hh in range(oh):
            for ww in range(ow):
                if hh != 0:
                    cost[hh][ww] = min(cost[hh][ww], cost[hh - 1][ww] + c)
                    cost[hh][ww] = min(cost[hh][ww], maze[hh - 1][ww] + c)
                if ww != 0:
                    cost[hh][ww] = min(cost[hh][ww], cost[hh][ww - 1] + c)
                    cost[hh][ww] = min(cost[hh][ww], maze[hh][ww - 1] + c)
                if hh == 0 and ww == 0:
                    continue
                res = min(res, cost[hh][ww] + maze[hh][ww])
        for h in range(oh):
            maze[h].reverse()
        # もう一回上のルーム回す



        cost = [[10**18] * ow for _ in range(oh)]
        cost[0][0] = maze[0][0]
        for hh in range(oh):
            for ww in range(ow):
                if hh != 0:
                    cost[hh][ww] = min(cost[hh][ww], cost[hh - 1][ww] + c)
                    cost[hh][ww] = min(cost[hh][ww], maze[hh - 1][ww] + c)
                if ww != 0:
                    cost[hh][ww] = min(cost[hh][ww], cost[hh][ww - 1] + c)
                    cost[hh][ww] = min(cost[hh][ww], maze[hh][ww - 1] + c)
                if hh == 0 and ww == 0:
                    continue
                #print(hh, ww, cost[hh][ww] + maze[hh][ww])
                res = min(res, cost[hh][ww] + maze[hh][ww])


        print(res)
        #pprint(cost)

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
        input = """3 4 2
1 7 7 9
9 6 3 7
7 8 6 4"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 1000000000
1000000 1000000 1
1000000 1000000 1000000
1 1000000 1000000"""
        output = """1001000001"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2 2
7 1
1 7"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()