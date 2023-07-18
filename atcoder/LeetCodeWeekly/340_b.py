from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prev = defaultdict(int) # 前に見つけた位置
        nokori = defaultdict(int) # のこりは？
        sugita = defaultdict(int) # 次にいくつある？
        total = defaultdict(int) # 現在帰せばいい値
        for i in range(len(nums)):
            x = nums[i]
            nokori[x] += 1
            total[x] += i
        #print(nokori)
        #print(total)
        ans = []
        for i in range(len(nums)):
            x = nums[i]
            total[x] -= nokori[x] * (i - prev[x])
            total[x] += sugita[x] * (i - prev[x])
            ans.append(total[x])
            nokori[x] -= 1
            sugita[x] += 1
            prev[x] = i
        #print(ans)
        return ans



st = Solution()

print(st.distance(nums = [1,3,1,1,2])== [5,0,3,4,0])
print(st.distance(nums = [0,5,3])==[0,0,0])

