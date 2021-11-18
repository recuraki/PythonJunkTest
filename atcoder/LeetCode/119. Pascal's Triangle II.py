class Solution:
    def getRow(self, numRows: int):
        l = [1]
        for i in range(numRows ):
            newl = [1]
            for j in range(len(l) - 1):
                newl.append(l[j] + l[j+1])
            newl += [1]
            l = newl
        return l
