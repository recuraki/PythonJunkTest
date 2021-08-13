from typing import List, Tuple
from pprint import pprint


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        npath = len(paths)
        from collections import defaultdict, deque
        G = [defaultdict(int) for _ in range(n)]
        Grev = [defaultdict(int) for _ in range(n)]
        for path in paths:
            for i in range(len(path) - 1):
                cur, next = path[i], path[i+1]
                G[cur][next] += 1 # 順辺
                Grev[next][cur] += 1 # ぎゃz九辺
        #print(G)

        allinclude = set(range(n))
        for path in paths:
            allinclude = allinclude.intersection(set(path))

        q = deque([])
        visited = [False]
        longestpath = [0] * n
        for cur in range(n):
            #print("Check", cur)
            existBackFullpath = False
            goodPaths = []
            for parent in Grev[cur].keys():
                if Grev[cur][parent] == npath:
                    existBackFullpath = True
                    break
            if existBackFullpath: # もし、nの辺があるなら候補じゃない
                continue
            #print(" > no backpath")
            for next in G[cur].keys():
                #print("check next ", next, G[cur][next])
                if G[cur][next] == npath:
                    q.append(cur)
        #print(q)

        walkpath = deque([])
        while len(q) > 0:
            first = q.pop()
            x = (first, 1)
            walkpath.append( x )
            #print("walk", walkpath)
            while len(walkpath) > 0:
                cur, level = walkpath.pop()
                #print(">> ", cur, level)
                longestpath[cur] = max(longestpath[cur], level)
                for next in G[cur].keys():
                    if G[cur][next] == npath:
                        x = (next, level + 1 )
                        walkpath.append( x )
        #print(longestpath)
        if max(longestpath) == 0:
            if len(allinclude) == 0:
                return 0
            else:
                return 1
            return
        return(max(longestpath))












st = Solution()

print(st.longestCommonSubpath( n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]) == 2)
print(st.longestCommonSubpath(n = 3, paths = [[0],[1],[2]]) == 0)
print(st.longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]) == 1)

