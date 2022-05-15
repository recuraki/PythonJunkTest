
from typing import List, Tuple, Optional
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        from collections import defaultdict
        nodeall = set()
        pcnt = defaultdict(int)
        leftnode = dict()
        rightnode = dict()
        for p, c, isLeft in descriptions:
            isLeft = True if isLeft==1 else False
            pcnt[c] += 1
            nodeall.add(p)
            nodeall.add(c)
            if isLeft:
                leftnode[p] = c
            else:
                rightnode[p] = c
        root = None
        pointer = dict()
        for node in nodeall:
            pointer[node] = TreeNode(node)
            if pcnt[node] == 0: root = node
        print(root)
        for node in nodeall:
            if node in leftnode: pointer[node].left = pointer[leftnode[node]]
            if node in rightnode: pointer[node].right = pointer[rightnode[node]]
        return pointer[root]





st = Solution()

print(st.createBinaryTree( [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])==0)

