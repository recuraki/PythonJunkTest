class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            shift = False
            if nums[l] % 2 == 0:
                l += 1
                shift = True
            if shift: continue
            if nums[r] % 2 == 1:
                r -= 1
                shift = True
            if shift: continue
            nums[l], nums[r] = nums[r], nums[l]
        return nums
