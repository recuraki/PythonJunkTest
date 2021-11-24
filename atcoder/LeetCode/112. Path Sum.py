# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
O(N), DFS超典型

WA: root-to-leafだった。
root-to-Nodeじゃなかった！
"""


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None and root.val == targetSum: return True
        ans = False
        if root.left is not None:
            ans = ans or self.hasPathSum(root.left, targetSum - root.val)
        if root.right is not None:
            ans = ans or self.hasPathSum(root.right, targetSum - root.val)
        return ans

