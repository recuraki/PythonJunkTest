# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
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
    #O(N)
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


class JoinAClub:
    def maximumClub(self, n, x, y):
        uf = UnionFindAtCoder(n)
        g = [set() for _ in range(n)]
        for i in range(len(x)):
            u, v = x[i], y[i]
            uf.Unite(u, v)
            g[u].add(v)
            g[v].add(u)
        #print(uf.roots())
        maxsize = -1
        maxroot = None
        for x in uf.roots():
            #print("root",x, uf.members(x))
            if len(uf.members(x)) > maxsize:
                maxsize = len(uf.members(x))
                maxroot = x
        res = []
        visited = [False] * n
        print(maxsize,maxroot)
        q = collections.deque([])
        q.append(maxroot)
        while len(q) > 0:
            curnode = q.popleft()
            if visited[curnode]: continue
            visited[curnode] = True
            res.append(curnode)
            for nextnode in g[curnode]:
                if visited[nextnode]: continue
                q.appendleft(nextnode)
        return tuple(res)

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(N, X, Y, __expected):
    startTime = time.time()
    instance = JoinAClub()
    exception = None
    try:
        __result = instance.maximumClub(N, X, Y);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("JoinAClub (400 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("JoinAClub.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            X = []
            for i in range(0, int(f.readline())):
                X.append(int(f.readline().rstrip()))
            X = tuple(X)
            Y = []
            for i in range(0, int(f.readline())):
                Y.append(int(f.readline().rstrip()))
            Y = tuple(Y)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, X, Y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1627143281
    PT, TT = (T / 60.0, 75.0)
    points = 400 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
