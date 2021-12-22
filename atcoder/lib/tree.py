class Node():
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

def recPreorder(root: Node):
    print(root.val, end=" ")
    if root.left: recPreorder(root.left)
    if root.right: recPreorder(root.right)


def nonrecPreorder(root: Node):
    st = []
    cur = root
    while True:
        if cur is not None:  # もし、今がノードにいるなら
            print(cur.val, end=" ")
            st.append(cur)  # 1個戻って、左をたどる。
            cur = cur.left
        elif len(st) > 0:  # 今が、葉で、親がいるなら、
            cur = st.pop()
            cur = cur.right
        else:
            break


def recInorder(root: Node):
    if root.left: recInorder(root.left)
    print(root.val, end=" ")
    if root.right: recInorder(root.right)


def nonrecInorder(root: Node):
    st = []
    cur = root
    while True:
        if cur is not None: # もし、今がノードにいるなら
            st.append(cur) # 1個戻って、左をたどる。
            cur = cur.left
        elif len(st) > 0: # 今が、葉で、親がいるなら、
            cur = st.pop()
            print(cur.val, end=" ")
            cur = cur.right
        else:
            break

def recPostorder(root: Node):
    if root.left: recPostorder(root.left)
    if root.right: recPostorder(root.right)
    print(root.val, end=" ")


def nonrecPostorder(root: Node):
    stDig = []
    stReverse = []
    stDig.append(root)
    while len(stDig) > 0:
        cur = stDig.pop()
        stReverse.append(cur)
        if cur.left: stDig.append(cur.left)
        if cur.right: stDig.append(cur.right)
    while len(stReverse) > 0:
        print(stReverse.pop().val, end = " ")






""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5
          / \
         6   7"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

recPreorder(root)
print()
nonrecPreorder(root)
print()
recInorder(root)
print()
nonrecInorder(root)
print()
recPostorder(root)
print()
nonrecPostorder(root)
print()
