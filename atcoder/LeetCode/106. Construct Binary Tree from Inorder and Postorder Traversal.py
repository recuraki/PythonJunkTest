"""

          3
    /          \
   9          20
           /     \
        15       7
Input:
inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
###############################################
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: return None
        ans = TreeNode() # これが消すべきルートノードです
        rootnum = postorder[-1]  # これが一番若いので、ルートになるノードのvalです
        # inorderでこれが見つかる場所を探す。
        # こうすると、そこを中心に左がleft, 右がrightと分かる
        for i in range(len(inorder)):
            if inorder[i] != rootnum: continue
            rootind = i
            break
        ans.val = rootnum # なんで値を入れる
        # 次に、inorderを左右に分割します。これはシンプル。
        intreeL = inorder[:rootind]
        intreeR = inorder[rootind + 1:]
        intreeLset = set(inorder[:rootind])
        intreeRset = set(inorder[rootind + 1:])
        # で、pretreeを復元する。preorderは順序を維持しながら左右に分けたい。
        posttreeL = []
        posttreeR = []
        for x in postorder:
            if x == rootnum:
                continue
            elif x in intreeLset:
                posttreeL.append(x)
            elif x in intreeRset:
                posttreeR.append(x)
        ans.left = self.buildTree(intreeL, posttreeL)
        ans.right = self.buildTree(intreeR, posttreeR)
        return ans
