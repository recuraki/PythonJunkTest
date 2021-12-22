
class Solution:
    def isArmstrong(self, n: int) -> bool:
        on = n
        k = 0
        while n > 0:
            n //= 10
            k += 1
        n = on
        ans = 0
        while n > 0:
            ans += (n%10) ** k
            n //= 10
        return on == ans