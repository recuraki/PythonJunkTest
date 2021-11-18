
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ss = set(arr)
        can = False
        zero = 0
        for x in arr:
            if x == 0: zero += 1
        for x in arr:
            if x == 0:
                if zero > 1: can=True
                continue
            if x*2 in ss: can=True
        return can