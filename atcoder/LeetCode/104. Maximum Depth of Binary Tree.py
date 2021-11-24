# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        ans = 0
        if root.left is not None:
            ans = max(ans, self.maxDepth(root.left))
        if root.right is not None:
            ans = max(ans, self.maxDepth(root.right))
        return ans + 1
