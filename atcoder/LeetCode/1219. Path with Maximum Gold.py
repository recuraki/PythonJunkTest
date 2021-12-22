class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dw = [0, -1, 1, 0]
        dh = [-1, 0, 0, 1]
        oh = len(grid)
        ow = len(grid[0])

        visited = [[False] * ow for _ in range(oh)]

        def dfs(ch, cw):
            # 0 then 0
            ans = 0
            if grid[ch][cw] == 0: return 0
            for di in range(len(dh)):
                nh = ch + dh[di]
                nw = cw + dw[di]
                if not (0 <= nh < oh): continue
                if not (0 <= nw < ow): continue
                if visited[nh][nw]: continue
                if grid[nh][nw] == 0: continue
                visited[nh][nw] = True
                ans = max(ans, dfs(nh, nw))
                visited[nh][nw] = False
            return ans + grid[ch][cw]

        ans = 0

        for initH in range(oh):
            for initW in range(ow):
                visited[initH][initW] = True
                score = dfs(initH, initW)
                ans = max(ans, score)
                visited[initH][initW] = False

        return ans
