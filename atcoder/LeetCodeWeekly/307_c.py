from typing import List, Tuple,Optional
from pprint import pprint


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        import collections
        g = collections.defaultdict(list)
        def dfs(root):
            if root.right != None:
                g[root.val].append(root.right.val)
                g[root.right.val].append(root.val)
                dfs(root.right)
            if root.left != None:
                g[root.val].append(root.left.val)
                g[root.left.val].append(root.val)
                dfs(root.left)
        dfs(root)
        #for i in range(20):
        #    print(i, g[i])
        import collections
        ans = 0
        q = collections.deque( [(start, 0)] )
        visited = set()
        visited.add(start)
        while len(q) > 0:
            curnode, curtime = q.popleft()
            ans = max(ans, curtime)
            for nxtnode in g[curnode]:
                if nxtnode in visited: continue
                q.append( (nxtnode, curtime+1) )
                visited.add(nxtnode)

        return ans




