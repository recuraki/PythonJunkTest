from typing import List, Tuple
from pprint import pprint


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(digits)
        ans = []
        for i in range(100, 1000, 2):
            s = str(i)
            can = True
            for j in range(10):
                need = s.count(str(j))
                if need > c[j]:
                    can = False
                    break
            if can: ans.append(i)
        ans.sort()
        return (ans)



st = Solution()

print(st.findEvenNumbers(digits = [2,1,3,0]))
print(st.findEvenNumbers(digits = [2,2,8,8,2]))
print(st.findEvenNumbers(digits = [3,7,5]))
print(st.findEvenNumbers(digits = [0,2,0,0]))
print(st.findEvenNumbers(digits = [0,0,0]))
