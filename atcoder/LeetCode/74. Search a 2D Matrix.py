class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_left
        for l in matrix:
            if l[0] <= target <= l[-1]:
                i = bisect_left(l, target)
                if l[i] == target: return True
        return False
