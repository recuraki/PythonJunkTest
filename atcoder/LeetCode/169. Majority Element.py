class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for x in nums: d[x] += 1
        dat = []
        for k in d: dat.append( (-d[k], k) )
        dat.sort()
        return(dat[0][1])