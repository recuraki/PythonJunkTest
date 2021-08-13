import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import collections
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        C = collections.Counter(dat)
        can = True
        buf = []
        for k in C.keys():
            if k % 2 != 0:
                print("NO")
                return
            if C[k] != 2:
                print("NO")
                return
            buf.append(k)
        buf.sort()
        p = -1
        dd = []
        for i in range(1, n):
            delta = buf[i] - buf[i-1]
            #if delta == p:
            #    print("NO")
            #    return
            dd.append(delta)
            p = delta
        ss = set()
        for i in range(len(dd)):
            d = 2*(i+1)
            if dd[i] % d != 0:
                print("NO")
                return
        k = buf[0] // 2
        res = []
        res.append(0)
        for i in range(len(dd)):
            delta = dd[i] // (2*(i+1))
            res.append(res[-1] + delta)


        sss = sum(res)
        if (k - sss) %  n==0:
            a = map(lambda x: x + (k-sss)//n, res)
            ss = set()
            for x in a:
                if x <1:
                    print("NO")
                    return

                if x in ss:
                    print("NO")
                    return
                ss.add(x)
            print("YES")


        else:
            print("NO")




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
        input = """6
2
8 12 8 12
2
7 7 9 11
2
7 11 7 11
1
1 1
4
40 56 48 40 80 56 80 48
6
240 154 210 162 174 154 186 240 174 186 162 210"""
        output = """YES
NO
NO
NO
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()