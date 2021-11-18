# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        方針基本的に、一蓮托生で見ていく。
        """

        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            # もしも、なにもないならNoneを返す
            if root1 == root2 == None: return None
            # そうでないなら子がいるので
            ans = TreeNode()
            if root1 is not None: ans.val += root1.val
            if root2 is not None: ans.val += root2.val
            if root1 is not None and root2 is not None:
                ans.left = dfs(root1.left, root2.left)
                ans.right = dfs(root1.right, root2.right)
            if root1 is None and root2 is not None:
                ans.left = root2.left
                ans.right = root2.right
            if root1 is not None and root2 is None:
                ans.left = root1.left
                ans.right = root1.right

            return ans

        return dfs(root1, root2)
