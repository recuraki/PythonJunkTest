class Solution:
    def countLetters(self, s: str) -> int:
        cnt = 0
        char = None
        ans = 0
        for x in s:
            if char == x:
                cnt += 1
            else:
                ans += (cnt * (cnt + 1)) // 2
                cnt = 1
                char = x
        ans += cnt * (cnt + 1) // 2
        return ans
