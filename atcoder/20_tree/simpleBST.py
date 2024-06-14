
class simpleBSTnode():
    def __init__(self, init: int = None) -> None:
        self.value = init
        self.left:simpleBSTnode = None
        self.right:simpleBSTnode = None
        self.p:simpleBSTnode = None # parent
        self.pp: simpleBSTnode = None # grand parent
        self.size = 1 # そのノードを含む部分木のサイズ

    def getMinNode(self): # 最小の値というのは一番左のノード
        cur = self
        while cur.left is not None: cur = cur.left
        return cur

    def getMaxNode(self): # 最大の値というのは一番右のノード
        cur = self
        while cur.right is not None: cur = cur.right
        return cur


class simpleBST():
    root: simpleBSTnode = None

    def __init__(self) -> None:
        pass


    def inorder(self):
        self.inorderco(self.root)
        print()

    def inorderco(self, x: simpleBSTnode):
        if x is None: return
        self.inorderco(x.left)
        print(x.value, end=' ')
        self.inorderco(x.right)
    def dump(self):
        self.dumpco(self.root)
        print()
        print(f"minnode {self.root.getMinNode().value}")
        print(f"maxnode {self.root.getMaxNode().value}")

    def dumpco(self, x: simpleBSTnode, depth = 0):
        if x is None: return
        s = f"[{depth}] cur = {x.value}"
        if x.left is not None: s += f", l = {x.left.value}"
        if x.right is not None: s += f", l = {x.right.value}"
        print(s)
        self.dumpco(x.left, depth+1)
        self.dumpco(x.right, depth+1)

    def search(self, x:int) -> simpleBSTnode:
        cur = self.root
        if cur is None: return None
        while cur is not None:
            if cur.value == x:
                return cur
            elif cur.value > x:
                cur = cur.left
            if cur.value < x:
                cur = cur.right
        return None

    # 次節点
    def successor(self, x:int) -> simpleBSTnode:
        cur = self.root
        if cur.right is not None:
            return self.getMinNode(cur.right)
        p = cur.p
        while p is not None and cur == p.right:
            cur = p
            p = p.p
        return cur

    def insert(self, val: int):
        nn = simpleBSTnode(val) # 新しいノードを作る
        cur = self.root # 挿入して良い点を検索する
        pcandidate = None # 探索を終えたノード
        while cur is not None:
            pcandidate = cur # 次を掘るので覚えておく
            if val < cur.value: cur = cur.left
            else: cur = cur.right
        nn.p = pcandidate
        if pcandidate is None: self.root = nn
        elif val < pcandidate.value: pcandidate.left = nn
        else: pcandidate.right = nn

    def transplant(self, u: simpleBSTnode, v: simpleBSTnode) -> None:
        #  部分木uをを部分木vにする。つまり、親からぶら下がっている先をvに変える
        # ここで注意するのはvalueがleft/rightでいいのかの確認は行わない
        if u.p is None: self.root = u # 根を全部置き換える = rootを置き換える
        elif u == u.p.left: u.p.left = v
        else: u.p.right = v
        # そして、vの親はuの親を引つぐ
        if v is not None: v.p = u.p

    """
    deleteは難しくていくつかのパターンに分かれる
    transplant(u, v) : uを部分木vで置き換える処理
    を使う。まず、1,2は非常にわかりすい。
    1: targetがLを持たないのならばtarget.rightをtargetの代わりにすれば良い
     transplant(target, target.right)としてよい。
    2: targetがRを持たないのならばtarget.leftをtargetの代わりにすれば良い
     transplant(target, target.left)として良い

    3が特殊な例で、target.leftが存在して、r = target.rightが存在しており、
     r.leftがいない場合を考える。この場合、target.leftが探索後は
     次に探索されるべきノードはであり、r.rightが探索されれば良い。
     targetを(leftを持たない)yで置き換えてleftにtarget.leftを繋げれば良い

    4は3を包含するケースで実は3が特殊なケースであった。
        target.leftが存在して、r = target.rightが存在して、r.leftが存在する場合を考える。
        target.leftが処理された後、target.rightの探索が行われるので、
        target.rightの部分木に対して次に探索される部分がtargetの代わりにいなければならない。
        target.rを根とする部分木が二分木であることは自明なので次に探索されるべきノードはmin(target.r)であるノードである。
        その後はtarget.rightの探索が行われれば良い。
        つまり、target.r =
        
    3 or 4を判定するためにはmi = min(r)をする。以下のとおり判定できる。
     mi == rであるときrはleftを持たない。つまり3。
     mi != rであるときrはleftをもち、mi = r.leftの部分木に含まれるノード。つまり4
    """
    def delete(self, target: simpleBSTnode) -> None:
        # targetのノードを削除する
        if target.left is None: self.transplant(target, target.right) # (1)
        elif target.right is None: self.transplant(target, target.left) # (2)
        else:
            r = target.right
            mi = r.getMinNode()
            if r != mi: # (4)の場合少し処理が必要
                self.transplant(mi, mi.right)
                mi.right = target.right
                mi.right.p = mi
            # (3) + 4の残りの処理
            self.transplant(target, mi)
            mi.left = target.left
            mi.left.p = mi



if __name__ == "__main__":
    sbst = simpleBST()
    sbst.insert(6)
    sbst.insert(5)
    sbst.insert(7)
    sbst.insert(2)
    sbst.insert(5)
    sbst.insert(8)
    sbst.inorder()
    sbst.dump()

    sbst = simpleBST()
    sbst.insert(2)
    sbst.insert(5)
    sbst.insert(7)
    sbst.insert(6)
    sbst.insert(8)
    sbst.insert(5)
    sbst.inorder()
    sbst.dump()

    

    
