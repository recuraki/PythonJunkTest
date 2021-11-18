
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        m = -1
        for x in nums:
            s.add(x)
            m = max(m, x)
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in s:
                ans.append(i)
        return ans