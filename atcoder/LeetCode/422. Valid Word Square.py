class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ma = 0
        for x in words: ma = max(ma, len(x))
        dat = []
        for x in words: dat.append(x + (" " * (ma - len(x))))
        print(dat)
        if len(words) != (ma): return False
        for i in range(ma):
            for j in range(ma):
                if dat[i][j] == dat[j][i]: continue
                return False
        return True