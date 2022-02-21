class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        nums = list(nums)
        nums.sort()
        ans = []
        cache = defaultdict(set)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while (r - l) > 0:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    if nums[l] in cache[nums[i]]:
                        l += 1
                        r -= 1
                        continue
                    ans.append([nums[i], nums[l], nums[r]])
                    cache[nums[i]].add(nums[l])
                    l += 1
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    r -= 1
        return ans
1