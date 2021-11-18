class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [0, -2, -1, -4, 0, -1, 1, 2, -3, 1]
        # 今いるところまでの累積和
        # これまでの累積和の最小値
        cum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            cum[i + 1] = cum[i] + nums[i]
        curmin = 0
        ans = -(2 ** 61)
        for i in range(1, len(nums) + 1):
            ans = max(ans, cum[i] - curmin)
            curmin = min(curmin, cum[i])
        return ans

