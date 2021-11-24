from collections import deque
#
class DinicRecurcive(object):
    INF = 2**60
    def __init__(self, n):
        """
        n: num of vertex
        """
        self.e = [[] for _ in range(n)]
        self.dist = [-1] * n
        self.iter = [-1] * n
        self.n = n

    def makeEdge(self, s, t, cap):
        l = [t, cap, None] # edge
        lrev = [s, 0, l] # reverse edge
        l[2] = lrev
        self.e[s].append(l)
        self.e[t].append(lrev)

    def bfs(self, s):
        self.dist[s] = 0 # init start point
        q = deque([])
        q.appendleft(s)
        while len(q) > 0:
            curNode = q.popleft()
            #print("curNode", curNode)
            for nextNode, edgeCap, revEdge in self.e[curNode]:
                #print("edgeCap", nextNode, edgeCap)
                if edgeCap > 0 and self.dist[nextNode] == -1:
                    self.dist[nextNode] = self.dist[curNode] + 1
                    q.appendleft(nextNode)

    def dfs(self, curNode, g, flow):
        if curNode == g:
            return flow

        for i in range(self.iter[curNode], len(self.e[curNode])):

            self.iter[curNode] += 1

            l = self.e[curNode][i] # node, cap, revpath

            # go only forward, don't back to parent
            if l[1] > 0 and self.dist[curNode] < self.dist[l[0]]:
                f = self.dfs(l[0], g, min(flow, l[1]))
                if f > 0:
                    l[1] -= f
                    l[2][1] += f
                    return f
        return 0

    def solve(self, s, g):
        """Max-Flow! """
        flow = 0
        while True:
            self.dist = [-1] * self.n
            self.bfs(s)
            if self.dist[g] == -1:
                return flow
            self.iter = [-1] * self.n
            while True:
                res = self.dfs(s, g, self.INF)
                #print("res", res)
                if res <= 0: # cannot more flow Then End
                    break
                flow += res

########################################################################

def domf():
    INF = 2**61
    while True:
        from collections import deque
        w, h = map(int, input().split())
        if w == h == 0: break
        maze = []
        curh, curw = -1, -1
        maze.append("#" * (w+2))
        for hh in range(h):
            l = list("#" + input() + "#")
            if l.count("@"): curh, curw = hh + 1, l.index("@")
            maze.append(l)
        maze.append("#" * (w+2))
        maze[curh][curw] = "."
        q = deque([(curh, curw)])
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]
        nodenum = (w + 2) * (h + 2) + 2
        nodes = nodenum - 2
        nodet = nodenum - 1
        hw2num  = lambda hh, ww: hh*(w+2) + ww
        mf = DinicRecurcive(nodenum)
        for hh in range(h+2):
            for ww in range(w+2):
                if maze[hh][ww] == "#": continue
                mf.makeEdge(hw2num(hh, ww), nodet, 1)
                for di in range(len(dh)):
                    mf.makeEdge(hw2num(hh, ww), hw2num(hh+dh[di], ww+dw[di]), h*w)
        mf.makeEdge(nodes, hw2num(curh, curw), h*w)
        print(mf.solve(nodes, nodet))
domf()