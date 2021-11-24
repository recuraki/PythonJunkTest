class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        x, y = points[0]
        for i in range(1, len(points)):
            ans += max(abs(x-points[i][0]), abs(y-points[i][1]))
            x, y = points[i]
        return ans