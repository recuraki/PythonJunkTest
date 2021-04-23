from typing import List, Tuple

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        cur = 0
        for x in nums:
            cur ^= x
        #print(">", x)
        first = True

        val = 0
        #print("target", bin(cur))
        for i in range(maximumBit):
            #print(" >", i)
            if ((cur >> i) & 1) == 0:
                #print("  ! yes")
                val += (2 ** i)
        #print("aa", val)
        res.append(val)

        for iii in range(len(nums) - 1):
            x = nums[len(nums) - 1 - iii]
            cur ^= x
            #print(">", x, cur)
            val = 0
            #print("target", bin(cur))
            for i in range(maximumBit):
                #print(" >", i)
                if ((cur >> i) & 1) == 0:
                    #("  ! yes")
                    val += (2 ** i)
            #print("aa", val)
            res.append(val)
        return res


st = Solution()

print(st.getMaximumXor(nums = [0,1,1,3], maximumBit = 2))
print(st.getMaximumXor(nums = [2,3,4,7], maximumBit = 3))
print(st.getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3))
print(st.getMaximumXor(nums = [0], maximumBit = 3))


