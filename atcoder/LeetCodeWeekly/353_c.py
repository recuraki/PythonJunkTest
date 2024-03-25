from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
# Paste the template of question
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[1,1] for _ in range(n)]
        ans = 1
        for i in range(n-1):
            #print(">", dp, nums1[i], nums1[i+1], nums2[i], nums2[i+1])
            if nums1[i] <= nums1[i+1]: dp[i+1][0] = max(dp[i+1][0], dp[i][0] + 1)
            #print(" ", dp)
            if nums1[i] <= nums2[i+1]: dp[i+1][1] = max(dp[i+1][1], dp[i][0] + 1)
            #print(" ", dp)
            if nums2[i] <= nums1[i+1]: dp[i+1][0] = max(dp[i+1][0], dp[i][1] + 1)
            #print(" ", dp)
            if nums2[i] <= nums2[i+1]:
                dp[i+1][1] = max(dp[i+1][1], dp[i][1] + 1)
            #print(" ", dp)



        ans = 0
        for l in dp: ans = max(ans, max(l))
        #print(dp)
        return ans




st = Solution()

print(st.maxNonDecreasingLength(nums1 = [2,3,1], nums2 = [1,2,1])==2)
print(st.maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4])==4)
print(st.maxNonDecreasingLength(nums1 = [3,19,13,19], nums2 = [20,18,7,14])==2)
print(st.maxNonDecreasingLength(nums1 = [5,16,15], nums2 = [12,1,14])==2)
print(st.maxNonDecreasingLength(nums1 = [8,7,4], nums2 = [13,4,4])==2)


