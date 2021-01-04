import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    # input = sys.stdin.readline
    from pprint import pprint
    import heapq
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        total = sum(dat)
        res = [total]
        buf = []
        imos = [0] * (n + 10)

        for i in range(n):
            buf.append([-dat[i], i])
        heapq.heapify(buf)
        usedColor = [{} for _ in range(n)]
        e = [[] for _ in range(n)]
        edgeColor = [None] * n

        for i in range(n - 1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            e[a].append([b, i])
            e[b].append([a, i])

        willColor = 0
        for i in range(n):
            w, curNode = heapq.heappop(buf)
            # print("Node", curNode, w)
            w = -w
            # print(w, curNode)
            tmp = []
            haveDefault = False
            for j in range(len(e[curNode])):
                nextNode, edgeIndex = e[curNode][j]
                if edgeColor[edgeIndex] is not None:
                    continue
                tmp.append([dat[nextNode], nextNode, edgeIndex])
            tmp.sort(reverse=False)  # good v
            # print("TMP", tmp)
            if len(tmp) != 0:
                _, nextNode, edgeIndex = tmp[0]
                willColor += 1
                # print("PAINT:", curNode, "->", nextNode, ":", willColor, "cost", max(dat[curNode], dat[curNode]))
                edgeColor[edgeIndex] = willColor
                imos[willColor] += dat[curNode]

        # print("imos", imos)
        cur = res[0]
        for i in range(n - 2):
            cur += imos[i + 1]
            res.append(cur)
        # print("!!!!!!!!!!!!")
        print(" ".join(list(map(str, res))))

    q = int(input())
    for _ in range(q):
        do()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff=100000
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
4
3 5 4 6
2 1
3 1
4 3
2
21 32
2 1
6
20 13 17 13 13 11
2 1
3 1
4 1
5 1
6 1
4
10 6 6 6
1 2
2 3
4 1"""
        output = """18 22 25
53
87 107 127 147 167
28 38 44"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()