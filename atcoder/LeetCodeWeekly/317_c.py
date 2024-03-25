from typing import List, Tuple
from pprint import pprint


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        s = str(n)
        s = list(s)
        s = list(reversed(s))
        s = list(map(int, s))
        for i in range(20):
            s.append(0)
        for ind in range(len(s)):
            while True:
                for keta in range(len(s)):
                    if s[keta] >= 10:
                        s[keta] = 0
                        s[keta+1] += 1
                if sum(s) <= target:
                    break
                s[ind] += 1
                isbre = False
                for keta in range(len(s)):
                    if s[keta] >= 10:
                        isbre = True
                        s[keta] = 0
                        s[keta+1] += 1
                if isbre: break

            if sum(s) <= target:
                break
        ret = map(str, list(reversed(s)))
        ret = "".join(ret)
        ret = int(ret)
        ans = ret - n
        #print(ans)
        return ans




st = Solution()

print(st.makeIntegerBeautiful(n = 16, target = 6)==4)
print(st.makeIntegerBeautiful(n = 467, target = 6)==33)
print(st.makeIntegerBeautiful(n = 1, target = 1)==0)
print(st.makeIntegerBeautiful(n = 204932336, target = 16)==67664)
print(st.makeIntegerBeautiful(n = 734504727, target = 10)==65495273)


