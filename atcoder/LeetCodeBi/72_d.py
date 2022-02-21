from typing import List, Tuple
from pprint import pprint

class BinaryIndexTreeSum:
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


# アルゴリズムイントロダクション 15.4 LCS
# Longest Common Subsequenceをとり、以下を返す
# b: 結果
# c: そこまでのlongestのcount(内部用)
def lcs_length(x, y):
    m, n  = len(x), len(y)
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"
    return c, b

# アルゴリズムイントロダクション 15.4 LCS
# bを基にもともとのinput xから共通部分を抜き出す。
def lcs_decode(b, X, i, j):
    import collections
    res = collections.deque([])
    while True:
        #print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
        if i == 0 or j == 0:
            break
        if b[i][j] == '↖':
            res.appendleft(X[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            i -= 1
            continue
        else:
            j -= 1
            continue
    return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        str1 = nums1
        str2 = nums2
        c, b = lcs_length(str1, str2)
        print(lcs_decode(b, str1, len(str1), len(str2)))


st = Solution()

#print(st.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))
#print(st.goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))
#print(st.goodTriplets([13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1], [8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]))
print(st.goodTriplets([13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1], [8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]) == 77)
print(st.goodTriplets(nums1 = [0,1,2,3,4,5,6], nums2 = [0,1,2,3,4,5,6]))
