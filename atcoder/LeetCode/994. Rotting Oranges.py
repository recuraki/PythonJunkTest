"""
全て腐るまでの秒数
= 腐らせて最後に判定、でよさそう
"""


class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        hh = len(mat)
        ww = len(mat[0])
        visited = [[1] * ww for _ in range(hh)]
        from collections import deque
        nextq = deque([])
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]
        for h in range(hh):
            for w in range(ww):
                if mat[h][w] == 0:
                    visited[h][w] = 0
                if mat[h][w] == 2:
                    nextq.append((h, w))
                    visited[h][w] = 2

        # print(nextq)
        turn = 0
        while len(nextq) > 0:
            q = nextq
            nextq = deque([])
            while len(q) > 0:
                h, w = q.pop()
                for di in range(len(dh)):
                    nh, nw = h + dh[di], w + dw[di]
                    if nh < 0 or hh <= nh: continue
                    if nw < 0 or ww <= nw: continue
                    if visited[nh][nw] != 1: continue
                    visited[nh][nw] = 2
                    nextq.append((nh, nw))
            if len(nextq) == 0: break
            turn += 1

        for h in range(hh):
            for w in range(ww):
                if visited[h][w] == 1: return -1

        return turn


