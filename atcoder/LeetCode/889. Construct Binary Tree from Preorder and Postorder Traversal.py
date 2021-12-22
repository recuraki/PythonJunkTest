"""

         1
    2        3
4     5   6     7

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

########################################################################
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0: return None

        ans = TreeNode()  # これが返すべきルートノードです
        rootnum = postorder[-1]  # これが一番若いので、ルートになるノードのvalです
        ans.val = rootnum  # なんで値を入れる

        # 長さが1の場合はそれで返す
        if len(preorder) == 1:
            return ans

        # preorderを作る
        # まず、postorderの[-2]っていうのは、右のroot nodeである
        rightrootval = postorder[len(postorder) - 2]
        preorderIndexRightNode = None
        for i in range(len(preorder)):
            if preorder[i] != rightrootval: continue
            preorderIndexRightNode = i
            break
        # で、preのそれを見つけたところまでが、preのLで、残りがR
        preorderL = preorder[1:preorderIndexRightNode]
        preorderR = preorder[preorderIndexRightNode:]

        # postorderを作る
        # preの[1]は[0]がrootなので、左のroot nodeである
        leftrootval = preorder[1]
        postorderIndexLeftNode = None
        for i in range(len(postorder)):
            if postorder[i] != leftrootval: continue
            postorderIndexLeftNode = i
            break
        # で、postのそこまでが、postのLで、残りがR
        postorderL = postorder[:postorderIndexLeftNode + 1]
        postorderR = postorder[postorderIndexLeftNode + 1: len(postorder) - 1]

        # ここが重要。線形(例えばRにしかない 1-2-3-4-5)なツリーの場合、
        # 上で、右のノードと左のノードがぐちゃぐちゃになっちゃう。
        # なので、右と左で同じツリーを作ろうとしてたら、ちゃんと消してあげる。
        if leftrootval == rightrootval:
            preorderL, preorderR = preorderR, preorderL

        ans.left = self.constructFromPrePost(preorderL, postorderL)
        ans.right = self.constructFromPrePost(preorderR, postorderR)
        return ans
