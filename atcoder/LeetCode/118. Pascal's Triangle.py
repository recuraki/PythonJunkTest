
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        l = [1]
        ans.append(l)
        for i in range(numRows - 1):
            newl = [1]
            for j in range(len(l) - 1):
                newl.append(l[j] + l[j+1])
            newl += [1]
            ans.append(newl)
            l = newl
        return ans
