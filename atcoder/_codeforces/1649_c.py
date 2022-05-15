
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

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
        oh, ow = map(int, input().split())
        maze = []
        for _ in range(oh):
            l = map(int, input().split())
            l = list(l)
            maze.append(l)
        from collections import defaultdict
        dlastind = defaultdict(int)
        dnum = defaultdict(int)
        dcost = defaultdict(int)
        ans = 0
        # 横を一列とみる
        for h in range(oh):
            curcnt = defaultdict(int)
            for w in range(ow):
                x = maze[h][w]
                curcnt[x] += 1
            for x in curcnt.keys():
                # cost
                dcost[x] += dnum[x] * (h - dlastind[x]) # さっきのに足されるコスト
                ans += dcost[x]  * curcnt[x]
                # after
                dlastind[x] = h
                dnum[x] += curcnt[x]

        dlastind = defaultdict(int)
        dnum = defaultdict(int)
        dcost = defaultdict(int)
        ans2 = 0
        for w in range(ow):
            curcnt = defaultdict(int)
            for h in range(oh):
                x = maze[h][w]
                curcnt[x] += 1
            for x in curcnt.keys():
                # cost
                dcost[x] += dnum[x] * (w - dlastind[x]) # さっきのに足されるコスト
                ans2 += dcost[x]  * curcnt[x]
                # after
                dlastind[x] = w
                dnum[x] += curcnt[x]

        print(ans + ans2)




    # 1 time
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
        input = """2 3
1 2 3
3 2 1"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4
1 1 2 2
2 1 1 2
2 2 1 1"""
        output = """76"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
1 1 2 3
2 1 1 2
3 1 2 1
1 1 2 1"""
        output = """129"""
        self.assertIO(input                     , output)


if __name__ == "__main__":
    unittest.main()