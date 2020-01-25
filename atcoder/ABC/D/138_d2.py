import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    sys.setrecursionlimit(1000000)
    n, q = map(int, input().split())
    cost = []
    res = []
    tree = []
    level = []
    childs = []
    parent = []
    cache = []
    for i in range(210000):
        res.append(0)
        tree.append([])
        level.append(-1)
        childs.append([])
        parent.append(-1)
        cost.append(0)
        cache.append(-1)

    for loop in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    def make_level(index, lev, pp):
        l = 0
        level[index] = lev
        parent[index] = pp
        for next in tree[index]:
            #print("index {0} search {1}".format(index, next))
            # 逆走はしない
            if level[next] != -1:
                #print("CANNOT MOVE to {0}".format(next))
                continue
            # 子供に親を設定
            parent[next] = index
            curparent = index
            make_level(next, lev + 1, index)

    make_level(1, 0, -1)

    for loop in range(q):
        p, x = map(int, input().split())
        cost[p] += x

    #print("parent")
    #print(parent[0:10])

    def calc_cost(index):
        if index == -1:
            return 0
        print("index = {0}, parent = {1}".format(index, parent[index]))
        if cache[parent[index]] != -1:
            print(" parent has cache: {0}".format(cache[parent[index]]))
            cache[index] = cost[index] + cache[parent[index]]
            print(" RET index = {0}, COST = {1}".format(index, cost[index] + cache[parent[index]]))
            return cost[index] + cache[parent[index]]
        else:
            cc = calc_cost(parent[index])
            print(" parent hasNOT cache: {0}".format(cc))
            cache[index] = cost[index] + cc
            print(" RET index = {0}, COST = {1}".format(index,cost[index] + cc))
            return cost[index] + cc



    for i in range(1, n+1):
        #print("llll:{0}".format(i))
        res[i] = calc_cost(i)

    res = list(map(str, res))
    print(" ".join(res[1:n+1]))

    #print(cost[0:10])
    #print(cache[0:10])

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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()