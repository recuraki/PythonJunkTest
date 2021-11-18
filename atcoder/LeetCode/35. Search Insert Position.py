class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # (ng, ok]: min
        nums += [2**61]
        ng = -1
        ok = len(nums)
        while abs(ok - ng) > 1:
            m = (ok + ng) // 2
            if nums[m] >= target: ok = m
            else: ng = m
        return ok