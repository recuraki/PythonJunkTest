



class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k+1)
        # index 0
        for i in range(min(k, len(piles[0]))):
            x = piles[0][i]
            dp[i+1] = dp[i] + x
        print(dp)
        for turn in range(1, len(piles)):
            newdp = [0] * (k+1)
            total = 0
            for i in range(1, min(k, len(piles[turn])) +1 ):
                total += piles[turn][i-1]
                newdp[i] = max(newdp[i], dp[i]) # 前のままをひきつぐ
                # ここまでというのはi個を取っているので
                newdp[i] = max(newdp[i-1] +0, 0)
            dp = newdp

        print(max(dp))




st = Solution()

print(st.maxValueOfCoins(piles = [[1,100,3],[7,8,9]], k = 2)==101)
print(st.maxValueOfCoins(piles = [[1,100,3],[7,8,9]], k = 10)==101)
print(st.maxValueOfCoins(piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7)==706)

