# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return None
        if root.val == val: return root
        ans = self.searchBST(root.left, val)
        if ans is not None: return ans
        ans = self.searchBST(root.right, val)
        if ans is not None: return ans
        return None
