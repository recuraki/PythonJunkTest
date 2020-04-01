import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    q = int(input())
    for _ in range(q):
        #print("------")
        n = int(input())
        dat = list(map(int, input().split()))
        dat = [dat[-1]] + dat

        lastSame = -1


        #print("datn", dat)
        pfig = dat[1]
        ccur = 0
        res = [0] * (n+1)
        res[1] = 1
        for i in range(2, n+1):
            #print("i", i, pfig, dat[i])
            if pfig == dat[i]:
                #print("same")
                ccur = 1
                lastSame = i
            else:
                #print("diff")
                if res[i - 1] == 1:
                    ccur = 2
                else:
                    ccur = 1
            res[i] = ccur
            pfig = dat[i]
        #print("origres")
        #print(res)
        if dat[1] != dat[0] and res[1] == res[-1]:
            if dat[0] != dat[1] and dat[1] != dat[2] and dat[0] != dat[2]:
                res[-1] = 3
            else:
                res[-1] = 2
        #print(res)
        c1 = max(res)
        s1 = " ".join(list(map(str, res[1:])))


        #print("datn", dat)
        pfig = dat[1]
        ccur = 0
        res = [0] * (n+1)
        res[1] = 1
        for i in range(2, n+1):
            #print("i", i, pfig, dat[i])
            if pfig == dat[i]:
                #print("same")
                ccur = 1 if lastSame != i else 2

            else:
                #print("diff")
                if res[i - 1] == 1:
                    ccur = 2
                else:
                    ccur = 1
            res[i] = ccur
            pfig = dat[i]
        #print("origres")
        #print(res)
        if dat[1] != dat[0] and res[1] == res[-1]:
            if dat[0] != dat[1] and dat[1] != dat[2] and dat[0] != dat[2]:
                res[-1] = 3
            else:
                res[-1] = 2
        #print(res)
        c2 = max(res)
        s2 = " ".join(list(map(str, res[1:])))


        if c1 <= c2:
            print(c1)
            print(s1)
        else:
            print(c2)
            print(s2)



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6
8
13 13 9 12 13 1 13 1
19
18 8 15 5 8 4 18 16 11 5 9 4 17 14 16 13 2 17 2
12
8 10 5 5 2 3 13 11 2 9 1 13
7
5 6 6 1 3 5 4
3
1 1 1
3
1 1 2"""
        output = """2
1 2 1 2 1 2 1 2 
3
1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 3
2
1 2 1 2 1 2 1 2 1 2 1 2 
2
2 1 1 2 1 2 1 
1
1 1 1 
2
1 1 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()