# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # [ok, ng) max
        ok = 1
        ng = n + 1
        while (abs(ok - ng) > 1):
            m = (ok + ng) // 2
            res = guess(m)
            if res == 0: return m
            if res == -1: ng = m
            if res == 1: ok = m
        return ok

