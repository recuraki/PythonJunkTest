class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #### O(N)
        from collections import deque
        ans = deque([])
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                ans.appendleft(nums[l] ** 2)
                l += 1
                continue
            # l > r
            ans.appendleft(nums[r] ** 2)
            r -= 1
        ans = list(ans)
        return ans

        #### O(NlogN)
        ans = []
        for x in nums:
            ans.append(x * x)
        ans.sort()
        return x