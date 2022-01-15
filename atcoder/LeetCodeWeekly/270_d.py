from typing import List, Tuple
from pprint import pprint


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import deque
        nodes = set()
        for a,b in pairs:
            nodes.add(a)
            nodes.add(b)
        n = len(nodes)
        zatsu = sorted(set(nodes))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newl = []
        for x in nodes:
            newl.append(zatsuTable[x])
        dat = []
        nodein = [deque([]) for _ in range(n)]
        nodeout = [deque([]) for _ in range(n)]
        for a, b, in pairs:
            a = zatsuTable[a]
            b = zatsuTable[b]
            nodeout[a].append(b)
            nodein[b].append(a)
        allsame = True
        nodes = -1
        for i in range(n):
            if len(nodeout[i]) != len(nodein[i]): allsame = False
            if len(nodeout[i]) + 1 == len(nodein[i]): nodet = i
            if len(nodeout[i]) == len(nodein[i]) + 1: nodes = i
        #print(nodes, nodet)
        if allsame is False:
            pass
            #print(zatsuTableRev[nodes], zatsuTableRev[nodet])
        else:
            nodes = 0
        trail = deque([])
        #print(nodeout)
        def dfs(u):
            while(len(nodeout[u]) > 0):
                v = nodeout[u].popleft()
                dfs(v)
            trail.appendleft(u)
        dfs(nodes)

        #print(trail)
        ans = []
        for x in trail:
            ans.append(zatsuTableRev[x])
        #print(ans)
        res = []
        for i in range(len(ans) - 1):
            res.append( [ans[i], ans[i+1]] )
        return res








st = Solution()

print(st.validArrangement(pairs = [[5,1],[4,5],[11,9],[9,4]]))
print(st.validArrangement(pairs = [[1,3],[3,2],[2,1]]))
print(st.validArrangement(pairs = [[1,2],[1,3],[2,1]]))
print(st.validArrangement(pairs = [[1,2]]))

