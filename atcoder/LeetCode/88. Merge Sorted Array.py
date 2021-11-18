class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        pos = len(num1) - 1
        pos1 = m - 1
        pos2 = n - 1
        while pos1 >= 0 and pos2 >= 0:
            if num1[pos1] >= num2[pos2]:
                num1[pos] = num1[pos1]
                pos1 -= 1
            else:
                num1[pos] = num2[pos2]
                pos2 -= 1
            pos -= 1
        while pos1 >= 0:
            num1[pos] = num1[pos1]
            pos1 -= 1
            pos -= 1
        while pos2 >= 0:
            num1[pos] = num2[pos2]
            pos2 -= 1
            pos -= 1


