import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = []
    for i in range(n):
        x,y,z = map(int,input().split())
        dat.append([x,y,z])

    primINF = 10**30
    matrix = []
    numV = n

    for i in range(n):
        l = []
        a, b, c = dat[i]
        for j in range(n):
            if i == j:
                l.append(-1)
                continue
            p, r, q = dat[j]
            cst = abs(p-a) + abs(q - b) + max(0, r - c)
            l.append(cst)
        matrix.append(l)

    from pprint import pprint
    #return

    from copy import deepcopy
    fcost = deepcopy(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if fcost[i][k] != -1 and fcost[k][j] != -1:
                    fcost[i][j] = min(fcost[i][j], fcost[i][k] + fcost[k][j])

    numV = n
    visited = [False] * numV
    cost = [primINF] * numV # cost
    parent = [-1] * numV # parent node
    cur = 0

    cost[0] = 0
    parent[0] = -1

    while True:
        # 訪問済み隣接の最小コストのノードを探索する
        mincost = primINF
        for i in range(n):
            curmincost = cost[i] + fcost[cur][i]
            if visited[i] is False and curmincost < mincost:
                mincost = curmincost
                u = i
            #print("mst",u, mincost)
        # 見つからなければ終了する
        cur = u
        if mincost == primINF:
            break
        # 訪問済みにする
        visited[u] = True
        for v in range(n):
            if visited[v] is False and matrix[u][v] != -1:
                if matrix[u][v] < cost[v]:
                    cost[v] = matrix[u][v]
                    parent[v] = u

    res = 0
    isparent = [False] * n
    for i in range(n):
        if parent[i] != -1:
            #res += matrix[i][parent[i]]
            res += matrix[parent[i]][i]
            isparent[parent[i]] = True

    isparent[0] = True
    #pprint(isparent)

    extra = 10**18
    p, r, q = dat[0]
    for i in range(n):
        if isparent[i]:
            continue
        a, b, c = dat[i]
        cst = abs(p-a) + abs(q - b) + max(0, r - c)
        extra = min(extra, cst)

    extra = matrix[cur][0]
    print(res + extra)




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
0 0 0
1 2 3"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
0 0 0
1 1 1
-1 -1 -1"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584"""
        output = """6519344"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()