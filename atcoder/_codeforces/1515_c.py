import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    from heapq import heappop, heapify, heappush
    def do():
        n, m, x = map(int, input().split())
        dat = list(map(int, input().split()))
        towers = [[0, i] for i in range(m)]
        totalheight = [0] * m
        res = [-1] * n
        walls = []
        heapify(towers)
        for i in range(n):
            walls.append([dat[i], i])
        walls.sort(reverse=True)

        for wallh, wallind in walls:
            towerh, towerind = heappop(towers)
            totalheight[towerind] += wallh
            heappush(towers, [totalheight[towerind], towerind] )
            res[wallind] = towerind + 1

        if abs(max(totalheight) - min(totalheight)) > x:
            print("NO")
            return
        print("YES")
        print(" ".join(list(map(str, res))))
        #print(totalheight)

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
        input = """2
5 2 3
1 2 3 1 2
4 3 3
1 1 2 3"""
        output = """YES
1 1 1 2 2
YES
1 2 2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
4 2 3
1 1 1 7 """
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()