import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    sys.setrecursionlimit(4100000)

    n = int(input())
    dat =[]
    link = []
    for i in range(n+1):
        link.append([])
    cost = [-1] * (n + 1)

    for i in range(n - 1):
        a, b, c = map(int, input().split())
        dat.append((a, b, c))
        link[a].append((b,c))
        link[b].append((a,c))

    dat_q = []
    q, k = map(int, input().split())

    for i in range(q):
        x, y = map(int, input().split())
        dat_q.append((x,y))

    #print(link)

    def search(curcost, current):
        #print("cost{0}, pos {1}: ".format(curcost, current))
        cost[current] = curcost
        for npos, ncost in link[current]:
            if cost[npos] != -1:
                # 戻らない
                continue
            search(curcost + ncost, npos)

    search(0, k)

    #print(cost)
    for i in range(q):
        x,y = dat_q[i]
        print(cost[x] + cost[y])


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
        input = """5
1 2 1
1 3 1
2 4 1
3 5 1
3 1
2 4
2 3
4 5"""
        output = """3
2
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
1 2 1
1 3 3
1 4 5
1 5 7
1 6 9
1 7 11
3 2
1 3
4 5
6 7"""
        output = """5
14
22"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000
6 7 1000000000
7 8 1000000000
8 9 1000000000
9 10 1000000000
1 1
9 10"""
        output = """17000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()