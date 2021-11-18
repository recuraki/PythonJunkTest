class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        gold = dict()
        gold["I"] = 1
        gold["V"] = 5
        gold["X"] = 10
        gold["L"] = 50
        gold["C"] = 100
        gold["D"] = 500
        gold["M"] = 1000
        i = 0
        while i < (len(s) - 1):
            if s[i] == "I" and s[i + 1] == "V":
                ans += 4
                i += 1
            elif s[i] == "I" and s[i + 1] == "X":
                ans += 9
                i += 1
            elif s[i] == "X" and s[i + 1] == "L":
                ans += 40
                i += 1
            elif s[i] == "X" and s[i + 1] == "C":
                ans += 90
                i += 1
            elif s[i] == "C" and s[i + 1] == "D":
                ans += 400
                i += 1
            elif s[i] == "C" and s[i + 1] == "M":
                ans += 900
                i += 1
            else:
                ans += gold[s[i]]
            i += 1
        if i < len(s):
            ans += gold[s[i]]
        return ans

