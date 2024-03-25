from typing import List, Tuple
from pprint import pprint


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for kth, trim in queries:
            kth -= 1
            dat = []
            for i in range(len(nums)):
                dat.append( (int(nums[i][-trim:]), i) )
            dat.sort()
            #print(dat)
            #print(dat[kth][1])
            ans.append(dat[kth][1])
        return ans



st = Solution()

print(st.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]])== [2,2,1,0])
print(st.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]])==[3,0])

