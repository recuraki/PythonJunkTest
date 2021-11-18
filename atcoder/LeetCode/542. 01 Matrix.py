class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        hh = len(mat)
        ww = len(mat[0])
        visited = [[-1] * ww for _ in range(hh)]
        from collections import deque
        nextq = deque([])
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]
        for h in range(hh):
            for w in range(ww):
                if mat[h][w] == 0:
                    nextq.append((h, w, 0))
                    visited[h][w] = 0
        # print(nextq)
        while len(nextq) > 0:
            q = nextq
            nextq = deque([])
            while len(q) > 0:
                h, w, lv = q.pop()
                for di in range(len(dh)):
                    nh, nw = h + dh[di], w + dw[di]
                    if nh < 0 or hh <= nh: continue
                    if nw < 0 or ww <= nw: continue
                    if visited[nh][nw] != -1: continue
                    visited[nh][nw] = lv + 1
                    nextq.append((nh, nw, lv + 1))

        return visited


