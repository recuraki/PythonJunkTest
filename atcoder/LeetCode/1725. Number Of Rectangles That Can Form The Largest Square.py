class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        l = []
        for a,b in rectangles:
            l.append(min(a,b))
        m = max(l)
        return l.count(m)