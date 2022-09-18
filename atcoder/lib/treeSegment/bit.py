# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
# BITはその性質上、1indexedである。

class BinaryIndexTreeSum:
    #
    # BE
    #
    def __init__(self, n): # [1-n]を作る
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i): # [1-i]のsumを取る(閉区間なことに注意)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def addCloseClose(self, i, x):
        assert i > 0 # bitなので1-indexed
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def rangesumCloseOpen(self, i, j): # [i, j) の和 Close-Open
        assert i > 0 # bitなので1-indexed
        assert i <= j
        return self.sum(j-1) - self.sum(i-1)

class RangeUpdate:
    def __init__(self, n):
        self.p = BinaryIndexTreeSum(n + 1)
        self.q = BinaryIndexTreeSum(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sumCloseClose(self, s, t): # [s, t]
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s

l = [1,2,3,4,5]
bit = BinaryIndexTreeSum(len(l))
for i in range(len(l)):
    bit.add(i+1, l[i])
for i in range(len(l) + 1):
    print(i, bit.sum(i))
