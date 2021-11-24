class Solution:
    # ほぼ、ヒストグラムの最大長方形
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        from collections import deque
        q = deque([])
        for i in range(len(temp)):
            curtemp = temp[i]
            while len(q) > 0:
                if q[0][1] < curtemp:
                    ind, prevtemp = q.popleft()
                    ans[ind] = i - ind
                else: break
            q.appendleft( (i, curtemp) )
        return ans