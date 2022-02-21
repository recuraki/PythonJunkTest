from typing import List, Tuple
from pprint import pprint


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        def nCr(n, r):
            import math
            # nCrのr>nは組み合わせが存在しないので0を返す
            # raiseすべきのこともあるかも
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))


        import math
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)


        ans = 0
        dp = [0] * k
        ans = 0
        ansinit = 0
        for x in nums: dp[x%k]+=1
        print(dp)

        # 0を選んだ場合の処理
        #ansinit += nCr(dp[0], 2) # 0同士のペア
        ansinit += dp[0] * (dp[0] - 1) // 2# 0同士のペア
        ansinit += dp[0] * (len(nums) - dp[0]) # 0と何かを選んだ時の数
        print("init", ansinit)

        # 0よりも大きなモノを選んだ時の処理
        for i in range(1, k):
            lval = lcm(k, i) // i
            lval %= k
            if lval == k: continue # 採用できない
            #print("!", i, lval)
            loopval = 1
            used = set()
            while (lval * loopval) < k: # kを超えるまでは頑張る
                x = (lval * loopval) % k
                #print(i, x)
                if x == 0: break
                #if x in used: break
                #used.add(x)
                if x == i: # 同じ同士の場合
                    ans += nCr(dp[x], 2)
                    loopval += 1
                    continue
                ans += dp[i] * dp[x]
                loopval += 1
                #print("next", lval * loopval)

        return ans//2 + ansinit



st = Solution()

print(st.coutPairs(nums = [1,2,3,4,5], k = 2))
print(st.coutPairs(nums = [1,2,3,4], k = 5))
print(st.coutPairs([8,10,2,5,9,6,3,8,2], 6) == 18)
#print(st.coutPairs([8,10,2,5,9,6,3,8,2], 6))
print(st.coutPairs([10,10,6,9,3,7,4,3,8,8], 4)) # 27
