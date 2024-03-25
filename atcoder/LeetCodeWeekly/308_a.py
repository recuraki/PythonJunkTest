from typing import List, Tuple
from pprint import pprint


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        nums.sort()
        for target in queries:
            ans = 0
            l = 0
            x = 0
            for r in range(n):
                x += nums[r]
                while target < x:
                    x -= nums[l]
                    l += 1
                ans = max(ans, (r-l) + 1)
            ret.append(ans)
        return(ret)





st = Solution()
print(st.answerQueries(nums = [4,5,2,1], queries = [3,10,21])==[2,3,4])
print(st.answerQueries(nums = [2,3,4,5], queries = [1])==[0])
print(st.answerQueries([736411,184882,914641,37925,214915], [331244,273144,118983,118252,305688,718089,665450]) == [2,2,1,1,2,3,3])
