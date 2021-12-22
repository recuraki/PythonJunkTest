class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        dat = defaultdict(set)
        for x, y in points: dat[x].add(y)
        ans = 2 ** 61
        allx = list(dat.keys())
        allx.sort()
        for i in range(len(allx)):
            for j in range(i + 1, len(allx)):
                under = allx[i]
                above = allx[j]
                candidate = list(dat[under] & dat[above])
                candidate.sort()
                for k in range(len(candidate) - 1):
                    ans = min(ans, (above-under) * (candidate[k+1] - candidate[k]))

        return ans if ans != 2**61 else 0      