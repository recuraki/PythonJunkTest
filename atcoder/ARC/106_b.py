import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    data =  list(map(int, input().split()))
    datb =  list(map(int, input().split()))
    lines = []

    e = []
    nodesperdepth = []
    for i in range(n):
        e.append([])
        nodesperdepth.append([])


    for _ in range(m):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        lines.append([c,d])
        e[c].append(d)
        e[d].append(c)

    rootnode = 0
    parentlist = [None] * n
    distlist = [-1] * n
    nodeval = [None] * n
    for i in range(n):
        nodeval[i] = datb[i] - data[i]

    # calc depth and parent node
    from collections import deque
    q = deque([])
    q.append([rootnode, -1, 0])
    while len(q) != 0:
        node, parent, d = q.popleft()
        parentlist[node] = parent
        distlist[node] = d
        nodesperdepth[d].append(node)
        for nextnode in e[node]:
            if parentlist[nextnode] is not None:  # parent
                continue
            q.append([nextnode, node, d + 1])

    print(nodesperdepth)
    print(nodeval)

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
        input = """3 2
1 2 3
2 2 2
1 2
2 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 0
5
5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 1
1 1
2 1
1 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """17 9
-905371741 -999219903 969314057 -989982132 -87720225 -175700172 -993990465 929461728 895449935 -999016241 782467448 -906404298 578539175 9684413 -619191091 -952046546 125053320
-440503430 -997661446 -912471383 -995879434 932992245 -928388880 -616761933 929461728 210953513 -994677396 648190629 -530944122 578539175 9684413 595786809 -952046546 125053320
2 10
6 12
9 11
11 5
7 6
3 15
3 1
1 9
10 4"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()