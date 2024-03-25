from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

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

###################################
# Paste the template of question
class Solution:
    def defdef(self):
        pass
###################################


st = Solution()

print(st.defdef(nums = [1,3,2,4,5])==2)
print(st.defdef(2)==1)

