"""
(()())(())
1212101210

"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        val = 0
        ans = ""
        for x in s:
            if x == "(":
                val += 1
                if val == 1: continue
            if x == ")":
                val -= 1
                if val == 0: continue
            ans += x
        return ans