from bisect import bisect_left


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = - (2 ** 61)
        curLen = 0
        ans = 0
        for val in nums:
            if val > prev:
                curLen += 1
                ans = max(ans, curLen)
            else:  # val <= prev
                curLen = 1
            prev = val
        return ans
