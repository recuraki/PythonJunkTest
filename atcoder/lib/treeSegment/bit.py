# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
# BITはその性質上、1indexedである。

class BinaryIndexTreeSum0Origin:
    def __init__(self, n): # [1-n]を作る
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i): # [0, i)のsumを取る
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def addPoint(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def rangesumCloseOpen(self, i, j): # [i, j) の和 Close-Open
        assert i <= j
        return self.sum(j-1) - self.sum(i-1)

class RangeUpdate0Origin:
    def __init__(self, n):
        self.p = BinaryIndexTreeSum0Origin(n + 1)
        self.q = BinaryIndexTreeSum0Origin(n + 1)

    def addPoint(self, s, x):
        self.addCloseOpen(s, s+1, x)

    def addCloseOpen(self, s, t, x):
        #t += 1
        self.p.addPoint(s, -x * s)
        self.p.addPoint(t, x * t)
        self.q.addPoint(s, x)
        self.q.addPoint(t, -x)

    def sumCloseOpen(self, s, t): # [s, t]
        #t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s

l = [1,2,3,4,5]
bit = BinaryIndexTreeSum0Origin(len(l))
for i in range(len(l)): bit.addPoint(i, l[i])

print("bit")
assert(bit.sum(2) == 6)
assert(bit.rangesumCloseOpen(1, 2+1) == 5)
assert(bit.rangesumCloseOpen(0, 0) == 0)
assert(bit.rangesumCloseOpen(0, 1) == 1)
assert(bit.rangesumCloseOpen(0, 4+1) == 15)

bit2 = RangeUpdate0Origin(6)
print(bit2.addCloseOpen(0, 1+1, 2))
print(bit2.sumCloseOpen(0, 5))
print(bit2.addPoint(0, 1))
print(bit2.sumCloseOpen(0, 5))
print(bit2.addPoint(3, 2))
print(bit2.sumCloseOpen(0, 5))
bit2.addCloseOpen(0, 5, 1)
print(bit2.sumCloseOpen(0, 5))
bit2.addCloseOpen(0, 5, -1)
print(bit2.sumCloseOpen(0, 5))
