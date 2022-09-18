from typing import List, Tuple
from pprint import pprint


class Solution:
    def largestPalindromic(self, num: str) -> str:
        import collections
        num = map(int, list(num))
        C = collections.Counter(num)
        ans = 0
        not0 = False
        odd = []
        gu = []
        for i in range(9, 0, -1):
            for _ in range(C[i] // 2): gu.append(i)
            if C[i] >= 2: not0 = True
            if C[i] % 2 == 1: odd.append(i)

        if not0: # 両端に0以外がある
            for _ in range(C[0] // 2): gu.append(0)

        if C[0] %2 == 1: odd.append(0)
        ans = []
        for x in gu: ans.append(x)
        if len(odd) > 0:
            odd.sort(reverse=True)
            ans.append(odd[0])
        for x in gu[::-1]: ans.append(x)

        if len(ans) == 0: ans= [0]
        ans = map(str, ans)
        #print("".join(ans))
        return "".join(ans)


st = Solution()

print(st.largestPalindromic(num = "444947137")=="7449447")
print(st.largestPalindromic(num = "00009")=="9")
print(st.largestPalindromic(num = "00001105")=="1005001")
print(st.largestPalindromic(num = "01")=="1")
print(st.largestPalindromic(num = "00")=="0")
print(st.largestPalindromic(num = "1")=="1")
print(st.largestPalindromic(num = "0")=="0")
print(st.largestPalindromic(num = "123")=="3")
print(st.largestPalindromic(num = "12300")=="3")
print(st.largestPalindromic(num = "123300")=="30203")
print(st.largestPalindromic(num = "1233")=="323")



