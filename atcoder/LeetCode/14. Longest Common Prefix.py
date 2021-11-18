class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            x = strs[0][i]
            for line in strs:
                if len(line) < (i+1): return ans
                if line[i] != x: return ans
            ans += x
        return ans
