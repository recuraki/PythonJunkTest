import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)


    def do():
        s = input()
        t = input()

        def dd(s):
            res = dict()
            for i in range(len(s)):
                #print("i", i)
                ss = s[:1+i]
                for j in range(1,21):
                    #print(s, (ss*j))
                    if s == (ss*j):
                        cnt = len(s) // len(ss)
                        #print(s, "can", ss, "=",cnt)
                        res[ss]=cnt
            return res
        slist = dd(s)
        #print(slist)
        tlist = dd(t)
        #print(tlist)
        reslen = 0
        resval = ""
        for k in list(slist.keys()):
            if k not in tlist:
                continue
            tmps = str(k) * lcm(slist[k] , tlist[k])
            if len(tmps) > reslen:
                reslen = len(tmps)
                resval = tmps

        if resval=="":
            print(-1)
        else:
            print(resval)



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
        input = """3
baba
ba
aa
aaa
aba
ab"""
        output = """baba
aaaaaa
-1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
baba
baba
"""
        output = """"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()