from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] += 1
        cur = 0
        res = [0]
        for x in nums:
            cur ^= x
            cnt[cur] += 1
            res.append(cur)
        #print(cnt)

        ans = 0
        cur = 0
        for x in nums:
            cur ^= x
            cnt[cur] -= 1
            ans += cnt[cur]
        #print(ans)
        #print(res)
        return ans



st = Solution()

print(st.beautifulSubarrays(nums = [4,3,1,2,4])==2)
print(st.beautifulSubarrays(nums = [3,1,2])==1)
print(st.beautifulSubarrays(nums = [0,3,1,2])==3)
print(st.beautifulSubarrays(nums = [0,0,3,1,2])==6)
print(st.beautifulSubarrays(nums = [1,10,4])==0)

