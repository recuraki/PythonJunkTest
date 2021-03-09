import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, k = map(int, input().split())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        dat1 = []
        dat2 = []
        for i in range(n):
            if datb[i] == 1:
                dat1.append(data[i])
            else:
                dat2.append(data[i])
        dat1.sort()
        dat2.sort()
        print(dat1)
        print(dat2)
        cur = sum(dat1)
        defo = sum(dat2)

        res = -1

        nextindj = 0
        for i in range(len(dat1)):
            print("i, cursum", i, cur)
            if cur > k:
                print ("NONO")
            while cur < k and nextindj < len(dat2):
                print("Check" ,cur, "+", dat2[nextindj])
                if (cur + dat2[nextindj]) <= k:
                    cur += dat2[nextindj]
                    nextindj += 1
                else:
                    break
            if cur <= k:
                pprint(dat1[:n-1-i])
                pprint(dat2[:nextindj])
                print("^^^^^^^^^^^^^")
                val = (1 * (len(dat1) - i) + (2 * (nextindj)))
                res = max(val, res)
            cur -= dat1[-1-i]
        print(defo - res, "ress")




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
        input = """5
5 7
5 3 2 1 4
2 1 1 2 1
1 3
2
1
5 10
2 3 2 3 2
1 2 1 2 1
4 10
5 1 3 4
1 2 1 2
4 5
3 2 1 2
2 1 2 1"""
        output = """2
-1
6
4
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()