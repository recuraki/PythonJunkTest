import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    """
      0
    3  1
     2
    """
    n = int(input())
    dat = list(map(int, input().split()))
    #dat.reverse()

    maze = []
    for i in range(n):
        for j in range(n):
            # nodeid,  umin, rmin, dmin, lmin, minall
            maze.append([0, 0, 0, 0, 0])
    #print(maze)

    import collections

    used = [False] * (n*n)
    umin = [0] * (n*n)
    lmin = [0] * (n*n)
    rmin = [0] * (n*n)
    dmin = [0] * (n*n)
    minall = [0] * (n*n)

    for i in range(n*n):
        u, l, r, d = i // n, i % n, (n-1) - (i%n), (n-1) - (i//n)
        umin[i] = min(u, 1 + l, 1 + r)
        dmin[i] = min(d, 1 + l, 1 + r)
        lmin[i] = min(l, 1 + u, 1 + d)
        rmin[i] = min(r, 1 + u, 1 + d)
        minall[i] = min(umin[i], dmin[i], lmin[i], rmin[i])

    finalcost = 0
    for ncustomer in dat:
        ncustomer -= 1 # 0 origin
        #print("next cus", ncustomer, "curcost", finalcost)
        #print(" > umin", umin)
        #print(" > lmin", lmin)
        #print(" > rmin", rmin)
        #print(" > dmin", dmin)
        #print(" > minall", minall)
        queue = collections.deque([])
        queue.append([ncustomer, -1])
        while len(queue) > 0:
            #print(" q", queue)
            nodeid, ngdirection = queue.popleft()
            needPropagete = False
            # 新しく３方向が閉じられたら伝搬
            if ngdirection == -1: # 新規OKなら絶対周囲に伝搬
                finalcost += minall[nodeid]
                needPropagete = True
            else: # 単なるOKの伝搬の時
                if ngdirection == 0:
                    umin[nodeid] -= 1
                elif ngdirection == 1:
                    rmin[nodeid] -= 1
                elif ngdirection == 2:
                    dmin[nodeid] -= 1
                elif ngdirection == 3:
                    lmin[nodeid] -= 1
                newmin = min(umin[nodeid], rmin[nodeid], lmin[nodeid], dmin[nodeid])
                if newmin < minall[nodeid]:
                    minall[nodeid] = newmin
                    needPropagete = True

            if needPropagete is True: # このノードが新規にダメになったらそれを伝搬
                if nodeid % n > 0 and ngdirection != 1: #l があるなら
                    queue.append([nodeid - 1, 1])
                if nodeid % n < (n-1) and ngdirection != 3: # rがあるなら
                    queue.append([nodeid + 1, 3])
                if nodeid // n > 0: #u があるなら
                    queue.append([nodeid - n, 2])
                if nodeid // n < (n-1): # dがあるなら
                    queue.append([nodeid + n, 0])

    print(finalcost)


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
1 3 7 9 5 4 8 6 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
6 7 1 4 13 16 10 9 5 11 12 14 15 2 3 8"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
11 21 35 22 7 36 27 34 8 20 15 13 16 1 24 3 2 17 26 9 18 32 31 23 19 14 4 25 10 29 28 33 12 6 5 30"""
        output = """11"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()