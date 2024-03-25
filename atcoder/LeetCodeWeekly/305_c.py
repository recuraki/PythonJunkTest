from typing import List, Tuple
from pprint import pprint


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = [False] * (n + 1)
        canReach[0] = True
        for i in range(n+1):
            if canReach[i] is False: continue
            if not (n - i) <= 2: # 3文字見える
                #print(i, i+1, i+2)
                if nums[i] == (nums[i + 1] - 1) == (nums[i + 2] - 2):
                    canReach[i+3] = True
                if nums[i] == (nums[i + 1]) == (nums[i + 2]):
                    canReach[i+3] = True
            if not (n - i) <= 1: # 2文字見える
                #print(i, i+1)
                if nums[i] == (nums[i + 1]):
                    canReach[i+2] = True
        #print(canReach)
        return canReach[-1]


    def validPartition2(self, nums: List[int]) -> bool:
        dat = []
        i = 0
        n = len(nums)
        while i < n:
            if (n - i) <= 2:
                dat.append(nums[i])
                i += 1
                continue
            if nums[i] == (nums[i+1]-1) == (nums[i+2]-2):
                i += 3
                continue
            dat.append(nums[i])
            i += 1
            continue

        import itertools
        print(dat)

        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]
        c = countstrs(dat)
        for a, b in c:
            if b == 1:
                return False
        return True



st = Solution()

print(st.validPartition(nums = [4,4,4,5,6])==True)
print(st.validPartition(nums = [4,5,6])==True)
print(st.validPartition(nums = [5,6])==False)
print(st.validPartition(nums = [5,5])==True)
print(st.validPartition(nums = [5,5,5])==True)
print(st.validPartition(nums = [5,5,5,5])==True)
print(st.validPartition(nums = [1,2,4])==False)
print(st.validPartition(nums = [1,1,1,2])==False)
print(st.validPartition(nums=[783377,783378,783379,783380,783381,783382,783383,783384,783385,783386,783387,783388,14925,14925,14925,190887,190887,190887,444668,444668,444668,444668,444669,444670,444671,444672,444673,444674]) == True)

