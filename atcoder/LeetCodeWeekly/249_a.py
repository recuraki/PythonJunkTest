from typing import List, Tuple
from pprint import pprint


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlist = []
        for x in nums:
            newlist.append(x)
        for x in nums:
            newlist.append(x)
        return newlist


st = Solution()

print(st.getConcatenation(nums = [1,2,1]))
print(st.getConcatenation(nums = [1,3,2,1]))
