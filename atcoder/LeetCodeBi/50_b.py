from typing import List, Tuple


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        import math
        for a, b, r in queries:
            r *= r
            cnt = 0
            for x, y in points:
                dis = (a-x)**2 + (b-y)**2
                if r >= dis:
                    cnt += 1
            res.append(cnt)
        return res


st = Solution()

print(st.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))
print(st.countPoints(points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))

