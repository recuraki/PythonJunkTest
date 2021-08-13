from typing import List, Tuple
from pprint import pprint


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        G = [[] for _ in range(n)]

        for cur in range(n):
            if prevRoom[cur] == -1:
                continue
            G[prevRoom[cur]].append(cur)
            G[cur].append(prevRoom[cur])

        q = []
        path = []
        pathdepth = []

        rootnode = 0
        depth = [-1] * n
        nodein = [-1] * n
        q.append([rootnode, 0])
        curtime = -1
        parent = [None] * n


        # q: nodenum, depth, vcost
        while len(q) != 0:
            curtime += 1
            curnode, curdepth = q.pop()
            if curnode >= 0:  # 行き掛け
                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                depth[curnode] = curdepth
                pathdepth.append(curdepth)
                path.append(curnode)
                for nextnode in G[curnode][::-1]:
                    if depth[nextnode] != -1:
                        continue
                    q.append([~curnode, curdepth])
                    q.append([nextnode, curdepth + 1])
                    parent[nextnode] = curnode
            else:
                curnode = ~curnode
                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                path.append(curnode)
                pathdepth.append(curdepth)
        print(path)

st = Solution()

print(st.waysToBuildRooms(prevRoom = [-1,0,1]))
print(st.waysToBuildRooms(prevRoom = [-1,0,0,1,2]))
