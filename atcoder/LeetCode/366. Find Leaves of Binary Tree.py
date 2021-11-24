.3# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
適当にしたから帰りの値をもらえば良さそう。
結果を返すので、他の関数を作る
"""
from collections import defaultdict
class Solution:
    ans = []
    def f(self, root: Optional[TreeNode]):
        if root is None: return -1
        lv = max(self.f(root.left), self.f(root.right)) + 1
        self.ans[lv].append(root.val)
        return lv

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = [list() for _ in range(101)]
        self.f(root)
        ansind = -1
        for i in range(101):
            if len(self.ans[i]) !=0: ansind = i
        return self.ans[:ansind+1]
