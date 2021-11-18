# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
自分自身のrecurciveでよさそう
returnするのは、自分のノードアドレス
自分は、子がいなくなって、自分がtargeの時、Noneを返す
"""


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left is not None: root.left = self.removeLeafNodes(root.left, target)
        if root.right is not None: root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target: return None
        return root

