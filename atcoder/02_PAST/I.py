import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = [1] * (2**n)
    datorig = list(map(int, input().split()))
    dat = []
    for i in range(len(datorig)):
        dat.append([i, datorig[i]])

    for i in range(1, n):
        #print(dat)
        #print(res)
        newdat = [None] * (2 ** (n - i) )
        for j in range(len(newdat)):
            if dat[2*j][1] > dat[2*j+1][1]: # 左の方が強ければ
                newdat[j] = [dat[2*j][0],dat[2*j][1]] # 勝ちあげて
                res[dat[2*j][0]] = i + 1 # 2回線に
            else: # ⇒が強い
                newdat[j] = [dat[2*j+1][0], dat[2*j+1][1]] # 勝ちあげて
                res[dat[2*j+1][0]] = i + 1# 2回線に
        dat = newdat

    print("\n".join(list(map(str, res))))

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
        input = """2
2 4 3 1"""
        output = """1
2
2
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
2 1"""
        output = """1
1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
4 7 5 1 6 3 2 8"""
        output = """1
3
2
1
2
1
1
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()