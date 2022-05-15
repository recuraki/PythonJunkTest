# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
############################################

# リストと仮定する
def transposes(s, t):
    assert len(s) == len(t)
    n = len(s)
    bit = Bit(len(s))
    ans = 0
    for i in range(i):
        ans += i - bit.sum()

