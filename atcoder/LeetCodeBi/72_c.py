from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []
        ans = []
        cur = 2
        total = 0
        while total + cur <= finalSum:
            ans.append(cur)
            total += cur
            cur += 2
        ans[-1] += finalSum - total
        return len(ans)



st = Solution()

print(st.maximumEvenSplit(finalSum = 12))
print(st.maximumEvenSplit(finalSum = 7))
print(st.maximumEvenSplit(finalSum = 10**10))
