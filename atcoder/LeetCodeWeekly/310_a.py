from typing import List, Tuple
from pprint import pprint


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        import collections
        C = collections.Counter(nums)
        ans = -1
        anscnt = -1
        for k in C.keys():
            if k%2 == 1: continue
            if C[k] > anscnt:
                anscnt = C[k]
                ans = k
                continue
            if C[k] == anscnt:
                if ans > k:
                    ans = k
        return ans



st = Solution()

print(st.mostFrequentEven(nums = [0,1,2,2,4,4,1])==2)
print(st.mostFrequentEven(nums = [4,4,4,9,2,4])==4)
print(st.mostFrequentEven(nums = [29,47,21,41,13,37,25,7])==-1)
print(st.mostFrequentEven(nums = [0,0,0,0,0])==0)


