import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        cnt = 1
        res = 0
        #print("---------")
        while cnt > 0:
            cnt = 0
            newdat = []
            avg = sum(dat) / len(dat)
            #print(">", dat, avg)
            for x in dat:
                #print(x, avg)
                if x > avg:
                    res += 1
                    cnt += 1
                else:
                    newdat.append(x)
            dat = newdat
        print(res)



    q = int(input())
    for _ in range(q):
        do()



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
        input = """4
6
1 1 1 2 2 3
6
9 9 9 9 9 9
6
6 4 1 1 4 1
1
1"""
        output = """3
0
3
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()