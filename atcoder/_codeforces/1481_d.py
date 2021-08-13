import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import heapq
    from collections import deque
    class dijkstra():
        INF = 2 ** 31 + 10000

        def __init__(self, numV):
            self.numV = numV
            self.e = [[] for _ in range(numV)]

        def makeEdge(self, s, t, cost):
            self.e[s].append((t, cost))

        def solve(self, nodeS, nodeT):
            self.distance = [self.INF] * self.numV
            self.cost = [self.INF] * self.numV  # cost
            self.parent = [-1] * self.numV  # parent node

            q = [(0, nodeS)]  # 初期ノード(cost 0)
            self.cost[nodeS] = 0
            heapq.heapify(q)
            while len(q) > 0:
                curcost, curnode = heapq.heappop(q)
                # if curcost > self.cost[curnode]:
                #    continue
                for nextnode, edgecost in self.e[curnode]:
                    nextcost = curcost + edgecost
                    if self.cost[nextnode] > nextcost:
                        self.cost[nextnode] = nextcost
                        self.parent[nextnode] = curnode
                        heapq.heappush(q, (nextcost, nextnode))

        def findRoute(self, s, t):
            # THIS FUNCTION should be called after solve()
            route = deque([])
            nextnode = t
            while nextnode != -1:
                route.appendleft(str(nextnode))
                nextnode = self.parent[nextnode]
            return route

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, m  = map(int, input().split())
        ea = [[] for _ in range(n)]
        eb = [[] for _ in range(n)]
        ga1 = dijkstra(n)
        ga2 = dijkstra(n)
        gb1 = dijkstra(n)
        gb2 = dijkstra(n)
        dat = []
        for i in range(n):
            s = input()
            dat.append(s) # all
            for j in range(n):
                if i == j:
                    continue
                if s[i] == "a":
                    ga1.makeEdge(i,j,1)
                    ga2.makeEdge(i,j,1)
                else:
                    gb1.makeEdge(i,j,1)
                    gb2.makeEdge(i,j,1)
        canLoop = False
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if dat[i][j] == dat[j][i]: # have aa or bb
                    res = []
                    for k in range(m):
                        res.append(i+1 if k%2 ==0 else j+1)
                    print("YES")
                    print(" ".join(list(map(str, res))))
                    return
        if m%2 == 1:
            res = []
            for k in range(m):
                res.append(2 if k % 2 == 0 else 1)
            print("YES")
            print(" ".join(list(map(str, res))))
            return

        can = False

        ga1.solve(0,0)
        ga2.solve(0,0)
        aFarVal = max(ga1.cost, ga2.cost)
        aFatInd = -1
        for i in range(n):
            if ga1.cost[i] == aFarVal:
                aFatInd = i
            if ga2.cost[i] == aFarVal:
                aFatInd = i
        if aFarVal != -1:
            ga1.solve(aFatInd,0)
            ga2.solve(aFatInd,0)
            t1 = max(ga1.cost)
            t2 = max(ga2.cost)
            aaFarVal = max(t1,t2)
            aaFatInd = -1
            for i in range(n):
                if ga1.cost[i] == aaFarVal:
                    aaFatInd = i
                if ga2.cost[i] == aaFarVal:
                    aaFatInd = i
            if aaFarVal != ga1.INF and aaFarVal >= m: # short m
                if aaFarVal in ga1.cost:
                    route = ga1.findRoute(aFatInd, aaFatInd)
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), route[:m]))))
                    return
                if aaFarVal in ga2.cost:
                    route = ga2.findRoute(aFatInd, aaFatInd)
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), route[:m]))))
                    return
            if dat[aaFatInd][aFatInd] == "a": # loop!
                route = ga2.findRoute(aFatInd, aaFatInd)
                res = []
                for i in range(m):
                    res.append(route[i % m])
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), res[:m]))))
                    return


        gb1.solve(0,0)
        gb2.solve(0,0)
        aFarVal = max(gb1.cost, gb2.cost)
        aFatInd = -1
        for i in range(n):
            if gb1.cost[i] == aFarVal:
                aFatInd = i
            if gb2.cost[i] == aFarVal:
                aFatInd = i
        if aFarVal != -1:
            gb1.solve(aFatInd,0)
            gb2.solve(aFatInd,0)
            t1 = max(gb1.cost)
            t2 = max(gb2.cost)
            aaFarVal = max(t1,t2)
            aaFatInd = -1
            for i in range(n):
                if gb1.cost[i] == aaFarVal:
                    aaFatInd = i
                if gb2.cost[i] == aaFarVal:
                    aaFatInd = i
            if  aaFarVal != ga1.INF and  aaFarVal >= m: # short m
                if aaFarVal in gb1.cost:
                    route = gb1.findRoute(aFatInd, aaFatInd)
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), route[:m]))))
                    return
                if aaFarVal in gb2.cost:
                    route = gb2.findRoute(aFatInd, aaFatInd)
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), route[:m]))))
                    return
            if dat[aaFatInd][aFatInd] == "b": # loop!
                route = gb2.findRoute(aFatInd, aaFatInd)
                res = []
                for i in range(m):
                    res.append(route[i % m])
                    print("YES")
                    print(" ".join(list(map(lambda x: str(x + 1), res[:m]))))
                    return
        print("NO")


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
3 1
*ba
b*b
ab*
3 3
*ba
b*b
ab*
3 4
*ba
b*b
ab*
4 6
*aaa
b*ba
ab*a
bba*
2 6
*a
b*"""
        output = """YES
1 2
YES
2 1 3 2
YES
1 3 1 3 1
YES
1 2 1 3 4 1 4
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()