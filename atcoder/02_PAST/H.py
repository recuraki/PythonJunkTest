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

    path[0].append( [numpointer[0][0][0], numpointer[0][0][1], 0] )
    if isfail is True:
        print(-1)
    else:
        for i in range(1, 11):
            for j in range(len(path[i-1])): # 前のステップ
                px, py, pc = path[i - 1][j]
                for k in range(len(numpointer[i])): # 今のステップ
                    cx, cy = numpointer[i][k]
                    cc = abs(px - cx) + abs(py - cy)
                    cc += pc
                    path[i].append([cx, cy, cc])
        #pprint(path)
        res = 9999999999999999
        for i in range(len(path[10])):
            res = min(res, path[10][i][2])
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