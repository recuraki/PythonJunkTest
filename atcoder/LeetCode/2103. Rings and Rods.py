class Solution:
    def countPoints(self, rings: str) -> int:
        dat = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            c, n = rings[i], int(rings[i + 1])
            dat[n].add(c)
        ans = 0
        for s in dat:
            if len(s) == 3: ans += 1
        return ans


rings = "B0R0G0R9R0B0G0"
