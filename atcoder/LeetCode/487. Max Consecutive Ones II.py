"""
計算量は0

  1 0 1 1 0 1 1 1 1
0 1 0 1 2 0 1 2 3 4
1 1 2 3 4 3 4 5 6 7

1 0 0 0 1 1
1 1 1
dpを持てばいい
dp[i][0] = ずっとひっくりかえさないで来た時の1の数
 0 でリセット = 0にする
 1 の時 前の[0] + 1
dp[i][1] = ただ一度、0をひっくり返した時の1の数
 0 のとき、前の[0] + 1
 1 の時、 前の[1] + 1
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        dp = [[None] * 2 for _ in range(n)]
        if nums[0] == 0:
            dp[0][0] = 0
            dp[0][1] = 1
        else:
            dp[0][0] = 1
            dp[0][1] = 1
        for i in range(1, n):
            if nums[i] == 0:
                dp[i][0] = 0
                dp[i][1] = dp[i - 1][0] + 1
            elif nums[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
            else:
                assert False
            ans = max(ans, dp[i][0], dp[i][1])
        return ans

