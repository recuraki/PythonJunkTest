from typing import List, Tuple, Optional
from pprint import pprint


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.route = deque([])
        self.route2target(root, startValue)
        #print(self.route)
        routes = "".join(self.route)
        self.route = deque([])
        self.route2target(root, destValue)
        #print(self.route)
        routed = "".join(self.route)
        #print(routes)
        #print(routed)

        def solve(routes, routet):
            if routes == "": return routet
            routet += "F" * max(0, len(routes) - len(routet))
            #print(routes)
            #print(routet)
            samelv = -1
            for i in range(len(routes)):
                if routes[i] == routet[i]:
                    samelv = i
                    continue
                break
            #print("same", samelv)
            ans = "U" * (len(routes) - samelv - 1)
            ans += routet[samelv + 1:]
            ans = ans.replace("F", "")
            #print("ans", ans)
            return ans
        return solve(routes, routed)

    def route2target(self, root: TreeNode, target: int):
        if root.val is None: return False
        if root.val == target: return True
        if root.left is not None:
            if self.route2target(root.left, target):  # Found!
                self.route.appendleft("L")
                return True
        if root.right is not None:
            if self.route2target(root.right, target):  # Found!
                self.route.appendleft("R")
                return True
        return False


st = Solution()

print(st.defdef())
