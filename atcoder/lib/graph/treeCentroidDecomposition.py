
# 重心分解
# https://ei1333.github.io/luzhiled/snippets/tree/centroid-decomposition.html
# O(N log N)
from collections import  deque
class centroidDecomposition():

    def __init__(self, vnum: int):
        self.vnum = vnum
        self.e = [[] for _ in range(vnum)]
        self.sub = [1] * vnum
        self.visited = [None] * vnum
        self.belong = []
        self.parent = [None] * vnum
        self.tourRoute = []

    def build(self, root: int = 0):
        # First DFS
        q = deque([])
        q.appendleft(root)
        self.tourRoute.append(root)
        self.parent[root] = -1 # root has no parent
        while len(q) > 0:
            curNode = q.popleft()
            print(curNode)
            if curNode >= 0: # Forward
                q.appendleft(~curNode)
                for nextNode in self.e[curNode]:
                    # NO reverse
                    if nextNode == self.parent[curNode]: continue
                    q.appendleft(nextNode)
                    self.parent[nextNode] = curNode
                    self.tourRoute.append(nextNode)
            else: # Reverse
                curNode = ~curNode
                print("reverse", curNode)
                print(">",self.parent[curNode], "+",self.sub[curNode])
                if self.parent[curNode] != -1:
                    self.sub[self.parent[curNode]] += self.sub[curNode]

        print(self.tourRoute)
        print(self.sub)




    def makeEdge(self, s:int, t:int):
        self.e[s].append(t)
        self.e[t].append(s)


def test():
    v = 9
    """
   0
   |
 +-+--+
 1    4
|+|  |+-|
2 3  5  8
    |+|
    6 7
    """
    edged = [(0,1),(1,2),(1,3),(0,4),(4,5),(4,8),(5,6),(5,7)]
    # tourRoute = [0, 1, 4, 2, 3, 5, 8, 6, 7]
    # print(sub = [9, 3, 1, 1, 5, 3, 1, 1, 1]
    cd = centroidDecomposition(v)
    for s,t in edged: cd.makeEdge(s,t)
    cd.build()

test()
