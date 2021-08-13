import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from heapq import heapify, heappop, heappush
    n, m, q = map(int, input().split())
    dat = []
    for _ in range(n):
        a, b = map(int, input().split())
        dat.append( (b, a))
    dat.sort(reverse=True)

    masterbox= list(map(int, input().split()))
    #print(dat)
    boxes = []
    res = [0] * q
    for i in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        l = []
        for i in range(m):
            if a<= i <= b:
                continue
            else:
                l.append(masterbox[i])

        l.sort()
        boxes.append(l)
    for value, siz in dat:
        #print(boxes)
        for ind in range(q):
            l = boxes[ind]
            if len(l) == 0:
                continue
            if l[-1] < siz:
                continue # 入らない
            cbox = len(l) - 1 # 選ぶボックス
            #print("queur", ind)
            while True:
                if l[cbox] < siz: # 入らないので
                    cbox += 1 #さっきのにする
                    break
                if cbox == 0: # 一番小さいのでいい
                    break
                cbox -= 1
            #print("i, used ind", siz, cbox, l[cbox])
            del l[cbox]
            res[ind] += value
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
        input = """3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3"""
        output = """20
0
9"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """3 4 3
1 9
2 9
7 8
1 8 6 9
4 4
1 4
1 3"""
        output = """26
0
9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()