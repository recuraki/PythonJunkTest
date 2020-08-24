import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    used = []
    for i in range(n+1):
        # visited, pv, cost
        used.append([False, None])
    path = []
    for i in range(n+1):
        path.append([])
    for i in range(m):
        a, b = map(int, input().split())
        path[a].append(b)
        path[b].append(a)

    import collections
    q = collections.deque([])
    q.append([1, -1, 0])
    #print(path)
    while len(q) > 0:
        #print("qu", q)
        curroom, pv, cost = q.popleft()
        #print("visit", curroom, used)
        #print(" > path", path[curroom])
        if used[curroom][0] is True:
            continue
        used[curroom][0] = True
        used[curroom][1] = pv
        for i in range(len(path[curroom])):
            nextroom = path[curroom][i]
            #print(" >> path[{0}] = {1}".format(path[curroom][i], nextroom))
            #print(" >>>>", used[nextroom])
            if used[nextroom][0] is True:
                #print(" >>!!visited")
                continue
            q.append([nextroom, curroom,cost])

    #print(used)


    can = True # 判定
    for i in range(1, n+1):
        x,y = used[i]
        if x is False:
            can = False

    if can is False:
        print("No")
    else:
        print("Yes")
        for i in range(2, n+1):
            print(used[i][1])



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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
1 2
2 3
1 2
2 1"""
        output = """No"""
if __name__ == "__main__":
    unittest.main()