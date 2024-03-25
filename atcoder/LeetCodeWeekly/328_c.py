from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        def get_pairs(count):
            return count*(count-1)//2 if count > 1 else 0

        N = len(nums)
        l = 0
        total_good = 0
        total_pairs = 0
        counter = Counter()
        for r, v in enumerate(nums):
            total_pairs += (get_pairs(counter[v] + 1) - get_pairs(counter[v]))
            counter[v] += 1

            while total_pairs >= k:
                total_good += N - r
                v = nums[l]
                total_pairs -= (get_pairs(counter[v]) - get_pairs(counter[v] - 1))
                counter[v] -= 1
                l += 1

        return total_good




st = Solution()

print(st.countGood(nums = [1,1,1,1,1], k = 10)==1)
print(st.countGood(nums = [3,1,4,3,2,2,4], k = 2)==4)
print(st.countGood(nums = [1]*(10**5), k = 2)==4)

