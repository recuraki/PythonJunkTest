class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s)):
            if s[i] != s[-1 - i]: return False
        return True
