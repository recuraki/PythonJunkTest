# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
# BITはその性質上、1indexedである。

class BinaryIndexTreeSum:
    #
    # BE
    #
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

