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
        l = int(input())
        s = input()
        dplcnt = [0] * l
        dplcost = [0] * l
        dprcnt = [0] * l
        dprcost = [0] * l
        for i in range(0, l - 1):
            if s[i] == "*":
                if i == 0:
                    dplcnt[i + 1] = 1
                    continue
                dplcnt[i + 1] = dplcnt[i] + 1
                dplcost[i + 1] = dplcost[i]
            else:
                if i == 0:
                    continue
                dplcnt[i + 1] = dplcnt[i]
                dplcost[i + 1] = dplcost[i] + dplcnt[i]
        for i in range(l - 1, 0, -1):
            if s[i] == "*":
                if i == 0:
                    dprcnt[i - 1] = 1
                    continue
                dprcnt[i - 1] = dprcnt[i] + 1
                dprcost[i - 1] = dprcost[i]
            else:
                if i == 0:
                    continue
                dprcnt[i - 1] = dprcnt[i]
                dprcost[i - 1] = dprcost[i] + dprcnt[i]
        res = 10 ** 18
        for i in range(l):
            if s[i] == "*":
                res = min(res, dprcost[i] + dplcost[i])
        res = 0 if res == 10 ** 18 else res
        print(res)
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
6
**.*..
5
*****
3
.*.
3
...
10
*.*...*.**"""
        output = """1
0
0
0
9"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()