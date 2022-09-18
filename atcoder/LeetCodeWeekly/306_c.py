from typing import List, Tuple
from pprint import pprint


class Solution:

    def smallestNumber2(self, pattern: str) -> str:
        tmp = [0]
        c = 0
        for x in list(pattern):
            if x == "I": c += 1
            elif x == "D": c -= 1
            else: assert False
            tmp.append(c)
        print(tmp)
    def smallestNumber(self, pattern: str) -> str:
        import itertools
        n = len(pattern)
        ans = 100000000000000000
        for pat2 in itertools.combinations(list(range(1, n + 2)), n+1):
            for pat in itertools.permutations(pat2):
                ok = True
                for i in range(n):
                    if pattern[i] == "D" and pat[i] <= pat[i+1]:
                        ok = False
                        break
                    elif pattern[i] == "I" and pat[i] >= pat[i+1]:
                        ok = False
                        break
                if ok:
                    ans = ""
                    for x in pat:
                        ans += chr(ord("0") + x)
                    print(ans)
                    return ans




st = Solution()

print(st.smallestNumber(pattern = "IIIDIDDD")=="123549876")
print(st.smallestNumber(pattern = "DDD")=="4321")

