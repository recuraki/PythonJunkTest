import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
from pprint import pprint

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    nume, k = map(int, input().split())

    # edgeの初期化 color, number, depth, value, forwardvalue
    # color: W(未訪問), G(探索中), B(探索済み)
    e = [ ["W", None, None, 1, 1] for _ in range(nume + 1)]
    numv = nume-1
    # 辺を張る
    v = [[] for _ in range(numv+10)]
    for _ in range(numv):
        s, t = map(int, input().split())
        #print(s,t)
        v[s].append(t)
        v[t].append(s)

    import collections
    q = collections.deque([])
    revq = collections.deque([])
    fowardq = collections.deque([])

    q.append([1, 0])
    revq.append(1)
    visited = [False]
    # pre calc
    while len(q) != 0:
        ce, depth = q.popleft()
        e[ce][0] = "B"
        e[ce][1] = ce
        e[ce][2] = depth
        visitcnt = 0
        for i in range(len(v[ce])):
            ne = v[ce][i]
            if e[ne][0] != "W":
                continue
            visitcnt += 1
            q.append([ne, depth + 1])
            revq.append(ne)
        if visitcnt == 0:
            e[ce][3] = 1
    #pprint(e)
    #print("rev")
    #pprint(revq)
    # calc
    while len(revq) != 0:
        ce = revq.pop()
        value = e[ce][3]
        for i in range(len(v[ce])):
            #print("ce", ce, "ne", ne, ":",e[ne][2] , e[ce][2])
            ne = v[ce][i]
            if e[ne][2] > e[ce][2]: # is child?
                #print("child", ne, e[ne])
                value += e[ne][3]
        e[ce][3] = value
    #pprint(e)
    dat = e[1:]
    #print(dat)
    # 3 = value, 2 = level
    #dat.sort(key=lambda x: (-x[2], x[3]))
    dat.sort(key=lambda x: (x[3], x[2]))
    #pprint(dat)
    target = dat[:k]
    #print(target)
    istarget = [False] * (nume + 1)
    for i in range(len(target)):
        istarget[target[i][1]] = True

    q = collections.deque([])
    q.append([1, 0])
    while len(q) != 0:
        ce, value = q.popleft()
        e[ce][0] = "G"
        if istarget[ce] is False:
            value += 1
        e[ce][4] = value
        for i in range(len(v[ce])):
            ne = v[ce][i]
            if e[ne][0] != "B":
                continue
            q.append([ne, value])


    #print("final")
    #print(target)
    #print(istarget)
    #pprint(e)
    #print(target)
    total = 0
    for i in range(len(target)):
        #print("node", target[i])
        total += target[i][4]
    print(total)






class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_10(self):
        print("test_input_10")
        input = """9 4
1 2
1 3
1 4
3 5
3 6
4 7
5 8
5 9"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """7 4
1 2
1 3
1 4
3 5
3 6
4 7"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 1
1 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 5
7 5
1 7
6 1
3 7
8 3
2 1
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """5 1
1 2
2 3
3 4
4 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_32(self):
        print("test_input_32")
        input = """5 2
1 2
2 3
3 4
4 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_33(self):
        print("test_input_33")
        input = """5 4
1 2
2 3
3 4
4 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_34(self):
        print("test_input_34")
        input = """5 4
1 2
1 3
1 4
1 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_35(self):
        print("test_input_35")
        input = """5 1
1 2
1 3
1 4
1 5"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()