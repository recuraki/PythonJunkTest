from typing import List, Tuple
from pprint import pprint

class sparseTable(object):
    func = None
    depthTreeList: int = 0
    table = []

    def __init__(self):
        self.table = []
        self.depthTreeList = 0

    def load(self, l):
        self.n = len(l)
        self.depthTreeList = (self.n - 1).bit_length() # Level
        self.table.append(l)
        for curLevel in range(1, self.depthTreeList):
            l = []
            for i in range( self.n - (2**curLevel -1) ):
                l.append(self.func(self.table[curLevel - 1][i], self.table[curLevel - 1][i + (2**(curLevel - 1)) ] ))
            self.table.append(l)

    def query(self, l, r): # [l, r)
        diff = r - l
        if diff <= 0:
            raise
        if diff == 1:
            return self.table[0][l]
        level = (diff - 1).bit_length() - 1
        return self.func(self.table[level][l], self.table[level][r - (2 ** level)])


class sparseTableMax(sparseTable):
    func = max


class sparseTableMin(sparseTable):
    func = min



class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        g = [set() for _ in range(len(parents))]
        n = len(parents)
        root = None
        for u in range(n):
            v = parents[u]
            if parents[u] == -1:
                root = u
                continue
            g[u].add(v)
            g[v].add(u)
        visited = [False] * n
        import collections
        q = collections.deque([])
        q.append(root)
        curtime = -1
        depth = [-1] * n
        nodein = [-1] * n
        nodeout = [-1] * n
        path = []

        while len(q) > 0:
            curtime += 1

            curnode = q.pop()
            if curnode >= 0: # go

                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                path.append(curnode)

                visited[curnode] = True

                if len(g[curnode]) == 1:  # 子がいないときの処理
                    nodeout[curnode] = curtime + 1

                for nextNode in g[curnode]:
                    if visited[nextNode]: continue
                    q.append(~curnode)
                    q.append(nextNode)


            else: # backward
                curnode = ~curnode
                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                path.append(curnode)
                nodeout[curnode] = curtime + 1

        print(nodein)
        print(nodeout)
        print(path)
        visittime = [[] for _ in range(n)]
        for i in range(len(path)):
            visittime[path[i]].append(i)


        stmin = sparseTableMin()
        stmax = sparseTableMax()
        stmin.load(path)
        stmax.load(path)
        from bisect import bisect_left

        for a,b in queries:
            print(a,b)
            ain = nodein[a]
            aout = nodeout[a]
            bin = nodein[b]
            bout = nodeout[b]
            if bin < ain:
                a,b = b,a
                ain, aout, bin, bout = bin, bout, ain, aout
            atrueout = bisect_left(visittime[a], bin)
            atrueout = visittime[a][atrueout-1]
            print("out in = " ,atrueout, bin)




st = Solution()

print(st.maxGeneticDifference(parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]))
print(st.maxGeneticDifference(parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]))
