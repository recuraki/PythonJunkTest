"""
     3
  9       20
1  2    15   7
             10

pre = [3, 9, 1, 2, 20, 15, 7, 10]

pre = [3, 9, 1, 2, 20, 15, 7, 10]
in  = [1, 9 2, 3,  15, 20, 10,7]

in  = [1, 9 2,---- 15, 20, 10,7]


     3
  9       20
1  2    15   7
             10
pre = [3, 9, 1, 2, 20, 15, 7, 10]
pre = [3, 9, 1, 2, 20, 15, 7, 10]
in  = [1, 9 2, 3,  15, 20, 10,7]
in  = [1, 9 2,---- 15, 20, 10,7]


    3
    9
    1
    2
pre = [3 9 1 2
in  = [2 1 9 3
基本的に、inorderだけあれば、左右が分かる。
なので、次が頭だ！というノードの情報さえあれば、よい。さて、
pre = [3, 9, 1, 2, 20, 15, 7, 10]
in  = [1, 9 2, 3,  15, 20, 10,7]
が与えられたとき、頭が3は自明なので、
 1, 9, 2
 15, 20, 10, 7
 にわける。で、その中で、最もpreorderが若いのは、
 1, [9], 2
 15, [20], 10, 7
 っていう風に再帰でいいのでは？
 で、範囲がiになっちゃったら、そのvalのノードを返せばいい
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        ans = TreeNode() # これが消すべきルートノードです
        rootnum = preorder[0]  # これが一番若いので、ルートになるノードのvalです
        # inorderでこれが見つかる場所を探す。
        # こうすると、そこを中心に左がleft, 右がrightと分かる
        for i in range(len(preorder)):
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
        pretreeL = []
        pretreeR = []
        for x in preorder:
            if x == rootnum:
                continue
            elif x in intreeLset:
                pretreeL.append(x)
            elif x in intreeRset:
                pretreeR.append(x)
        ans.left = self.buildTree(pretreeL, intreeL)
        ans.right = self.buildTree(pretreeR, intreeR)
        return ans
