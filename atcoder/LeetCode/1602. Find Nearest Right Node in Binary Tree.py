
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
O(N)でBFSかな。各ループごとにListを更新。
"""
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        from collections import deque
        nextq = deque([root])
        while len(nextq) > 0:
            q = nextq
            nextq = deque([])
            dat = [] # このレベルの左からのノード
            while len(q) > 0:
                curnode = q.popleft()
                dat.append(curnode)
                if curnode.left is not None: nextq.append(curnode.left)
                if curnode.right is not None: nextq.append(curnode.right)
            # 結果の確認(再度O N)
            if u not in dat: continue  # なかった
            if dat.index(u) == len(dat) - 1: return None # そのlvの右端
            return dat[dat.index(u) + 1]
        return None


