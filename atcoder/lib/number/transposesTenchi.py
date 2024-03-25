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

# 1,2,3...のリスト。0はダメ版
def transposes(s):
    n = len(s)
    bit = Bit(n)
    ans = 0
    for i in range(n):
        assert s[i] != 0
        ans += i - bit.sum(s[i])
        bit.add(s[i], 1)
    return ans

print(transposes([1,2,3]))
print(transposes([2,3,1]))
print(transposes([3,1,2]))
print(transposes([1,3,2]))
print(transposes([2,1,3]))
print(transposes([3,2,1]))
print("---")
print(transposes([1,2,3,4]))
print(transposes([4,2,3,1]))
print(transposes([3,2,1,4]))
print(transposes([5,2,3,4,1]))
print(transposes([1,2,3,4,5,6,7,8]))
print(transposes([1,7,3,4,5,6,2,8]))
print(transposes([7,2,3,4,5,6,1,8]))
print(transposes([7,2,3,4,5,6,8,1]))




