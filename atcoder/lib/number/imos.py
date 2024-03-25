"""
0-(n-1)のリストを作る
"""
class imos1d():
    def __init__(self, n):
        self.n = n
        self.res = [0] * n
    def add(self, ind, val):
        self.res[ind] += val
    def solve(self):
        for i in range(1,self.n): self.res[i] += self.res[i-1]

t = imos1d(10)
t.add(0, 1)
t.add(1, 2)
t.add(4, -1)
t.add(6, -2)
t.solve()
print(t.res)