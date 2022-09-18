from typing import List, Tuple
from pprint import pprint

###################################
# Paste the template of question
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        nokori = 0
        pair = 0
        for k in c.keys():
            pair += c[k] //2
            nokori += c[k] % 2
        return ([pair, nokori])


st = Solution()

print(st.numberOfPairs([1,3,2,1,3,2,2])==[3,1])
print(st.numberOfPairs([1,1])==[1,0])
print(st.numberOfPairs([0])==[0,1])

