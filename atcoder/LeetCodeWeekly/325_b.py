from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        if s.count("a") < k: return -1
        if s.count("b") < k: return -1
        if s.count("c") < k: return -1
        ans = len(s)
        cnt = [0, 0, 0]
        for x in s:
            x = ord(x) - ord("a")
            cnt[x] += 1
        r = 0
        n = len(s)
        for l in range(n):
            while cnt[0] >= k and cnt[1] >= k and cnt[2] >= k:
                #print(l, r, cnt)
                ans = min(ans, l + (n-r))
                if r >= n: break
                chrr = ord(s[r]) - ord("a")
                cnt[chrr] -= 1
                r += 1

            chrl = ord(s[l]) - ord("a")
            cnt[chrl] += 1

            while cnt[0] >= k and cnt[1] >= k and cnt[2] >= k:
                #print(l, r, cnt)
                ans = min(ans, l + (n-r)+1)
                if r >= n: break
                chrr = ord(s[r]) - ord("a")
                cnt[chrr] -= 1
                r += 1

        return ans









st = Solution()

print(st.takeCharacters(s = "aabaaaacaabc", k = 2)==8)
print(st.takeCharacters( s = "a", k = 1)==-1)
print(st.takeCharacters( s = "a", k = 0)==0)
print(st.takeCharacters("acba", 1) == 3)
print(st.takeCharacters("cbbac", 1) == 3)