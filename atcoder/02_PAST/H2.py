import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n, m = map(int, input().split())
    maze = []
    numpointer = []
    path = []

    for i in range(11):
        numpointer.append([])
        path.append([])

    cost = []
    for i in range(n):
        cost.append([9999999999] * m)

    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == "S":
                numpointer[0].append([i, j])
                continue
            if s[j] == "G":
                numpointer[10].append([i, j])
                continue
            else:
                numpointer[int(s[j])].append([i,j])
    #print(numpointer)
    isfail = False
    for i in range(11):
        if len(numpointer[i]) == 0:
            isfail = True

    # スタートのコストは0
    cost[numpointer[0][0][0]][numpointer[0][0][1]] = 0

    if isfail is True:
        print(-1)
    else:
        for i in range(1, 11):
            for j in range(len(numpointer[i-1])): # 前のポインタ
                px, py= numpointer[i-1][j]
                pc = cost[px][py]
                for k in range(len(numpointer[i])): # 今のステップ
                    cx, cy = numpointer[i][k]
                    cc = abs(px - cx) + abs(py - cy)
                    cc += pc
                    cost[cx][cy] = min(cost[cx][cy], cc)
        print(cost[numpointer[10][0][0]][numpointer[10][0][1]])

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
        input = """3 4
1S23
4567
89G1"""
        output = """17"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 11
S134258976G"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 3
S12
4G7
593"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()