class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        nums.sort()
        return math.gcd(nums[0], nums[-1])