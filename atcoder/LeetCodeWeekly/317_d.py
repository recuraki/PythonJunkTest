from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict




from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right




class Solution:
    edgeNum = []

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        from collections import deque
        from collections import deque

        n = 100000+10
        leftnode = [None] * n
        rightnode = [None] * n

        self.edgeNum = [0] * n
        g = defaultdict(list)
        parent = [-1] * n
        def dig(root, parentnode = -1):
            if root is None: return
            parent[root.val] = parentnode
            if root.left is not None:
                g[root.val].append(root.left.val)
                self.edgeNum[root.left.val] += 1
                leftnode[root.val] = root.left.val
            if root.right is not None:
                g[root.val].append(root.right.val)
                self.edgeNum[root.right.val] += 1
                rightnode[root.val] = root.right.val
            dig(root.left)
            dig(root.right)

        dig(root)

        q = deque([])
        ans = []
        for i in range(n):
            if (self.edgeNum[i] != 0): continue
            q.appendleft(i)
            ans.append(i)
        while (len(q) > 0):
            cur = q.popleft()
            for nxt in g[cur]:
                self.edgeNum[nxt] -= 1
                if self.edgeNum[nxt] == 0:
                    ans.append(nxt)
                    q.append(nxt)
        topo = ans
        leftcnt = [0] * n
        rightcnt = [0] * n
        parentcnt = [0] * n
        depth = [0] * n
        for nodenum in reversed(topo):
            if leftnode[nodenum] is not None:
                leftcnt[nodenum] = max(leftcnt[leftnode[nodenum]], rightcnt[leftnode[nodenum]]) + 1
            if rightnode[nodenum] is not None:
                rightcnt[nodenum] = max(leftcnt[rightnode[nodenum]], rightcnt[rightnode[nodenum]]) + 1

        ans = dict()
        for nodenum in topo:
            if leftnode[nodenum] is not None:
                depth[leftnode[nodenum]] = depth[nodenum] + 1
                parentcnt[leftnode[nodenum]] = max(depth[nodenum] + rightcnt[nodenum], parentcnt[nodenum])
            if rightnode[nodenum] is not None:
                depth[rightnode[nodenum]] = depth[nodenum] + 1
                parentcnt[rightnode[nodenum]] = max(depth[nodenum] +leftcnt[nodenum], parentcnt[nodenum])
        ans = []
        for x in queries:
            ans.append(parentcnt[x])
        return ans








