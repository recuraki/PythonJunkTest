from typing import List, Tuple
from pprint import pprint


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        mi = 10**18
        ma = -1
        def do(order, cnt, firstPlayer, secondPlayer):
            n = len(order)
            if n % 2 == 0:
                if firstPlayer >= (n // 2):
                    firstPlayer = n - 1 - firstPlayer
                if secondPlayer >= (n // 2):
                    secondPlayer = n - 1 - secondPlayer
            if n % 2 == 1:
                if firstPlayer > (n // 2):
                    firstPlayer = n - 1 - firstPlayer
                if secondPlayer > (n // 2):
                    secondPlayer = n - 1 - secondPlayer
            if firstPlayer == secondPlayer:
                return cnt
            for pat in range(1<< (n//2 - 2) ):

        return do(list(range(n)), 1, firstPlayer, secondPlayer)







st = Solution()

print(st.earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4))
print(st.earliestAndLatest( n = 5, firstPlayer = 1, secondPlayer = 5))
