import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class UnionFindAtCoder():
        # 作りたい要素数nで初期化
        # 使用するインスタンス変数の初期化
        def __init__(self, n):
            self.n = n
            # root[x]<0ならそのノードが根かつその値が木の要素数
            # rootノードでその木の要素数を記録する
            self.root = [-1] * (n + 1)
            # 木をくっつける時にアンバランスにならないように調整する
            self.rnk = [0] * (n + 1)
        # ノードxのrootノードを見つける
        def Find_Root(self, x):
            if (self.root[x] < 0):
                return x
            else:
                # ここで代入しておくことで、後の繰り返しを避ける
                self.root[x] = self.Find_Root(self.root[x])
                return self.root[x]

        # 木の併合、入力は併合したい各ノード
        def Unite(self, x, y):
            # 入力ノードのrootノードを見つける
            x = self.Find_Root(x)
            y = self.Find_Root(y)
            # すでに同じ木に属していた場合
            if (x == y):
                return
                # 違う木に属していた場合rnkを見てくっつける方を決める
            elif (self.rnk[x] > self.rnk[y]):
                self.root[x] += self.root[y]
                self.root[y] = x

            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                # rnkが同じ（深さに差がない場合）は1増やす
                if (self.rnk[x] == self.rnk[y]):
                    self.rnk[y] += 1
        # xとyが同じグループに属するか判断
        def isSameGroup(self, x, y):
            return self.Find_Root(x) == self.Find_Root(y)
        # ノードxが属する木のサイズを返す
        def Count(self, x):
            return -self.root[self.Find_Root(x)]
        # Listing all nodes same as group of x
        # O(N)
        def members(self, x):
            root = self.Find_Root(x)
            return [i for i in range(self.n) if self.Find_Root(i) == root]
        # List all root
        # O(N)
        def roots(self):
            return [i for i, x in enumerate(self.root) if x < 0]
        # root Count
        def group_count(self):
            return len(self.roots())
        # {4: [0, 1, 2, 3, 4, 5, 6, 8, 9], 7: [7], 10: []}
        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}
        def size(self, x):
            return -self.root[self.Find_Root(x)]

    lma = 400000
    n = int(input())
    uf = UnionFindAtCoder(lma + 10)
    count = [0] * (lma + 10)
    dat = []
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        count[a] += 1
        count[b] += 1
        uf.Unite(a,b)
        dat.append((a,b))
    rcount = [0] * (lma + 10)
    for a,b in dat:
        rcount[uf.Find_Root(a)] += 1
    res = 0
    for i in range(lma):
        if uf.Find_Root(i) == i:
            if uf.size(i) == rcount[i] + 1:
                res += uf.size(i) - 1
            else:
                res += uf.size(i)
    print(res)




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """4
1 2
1 3
4 2
2 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
111 111
111 111"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()