import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left
    def do():
        from copy import deepcopy
        n = int(input())
        dat = list(map(lambda x(-x), input().split()))
        #if n == 1:
            #print("YES")
            #print(dat[0], dat[1])
        dat.sort()
        odat = deepcopy(dat)

        for basei in range(1, 2*n):
            firstnum = dat[0] + dat[basei]
            hres = []
            hres.append( [dat[basei], dat[0]] )
            visited = [False] * (2*n)
            visited[0] = True
            visited[basei] = True
            curmax = dat[0]
            for loop in range(n - 1):
                isok = False
                for i in range(1, 2*n):
                    if visited: continue
                    x = dat[i]
                    need = curmax - x
                    ind = bisect_left(dat, need, lo=i + 1)
                    dame = False

                    if ind >= len(dat):
                        continue
                    if dat[ind] == need:
                        #print(">>hit!", i, ind , "val=", dat[i], dat[ind])
                        curmax = dat[ind]
                        hres.append( [dat[i], dat[ind]] )
                        isok = True
                        visited[ind] = True
                        visited[i] = True
                        break
                if isok is False:
                    can = False
                    break


        if can:
            print("YES")
            print(firstnum)
            for a,b in hres:
                print(a, b)
            return
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
        input = """4
2
3 5 1 2
3
1 1 8 8 64 64
2
1 1 2 4
5
1 2 3 4 5 6 7 14 3 11"""
        output = """YES
6
1 5
2 3
NO
NO
YES
21
14 7
3 11
5 6
2 4
3 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1
1 10000"""
        output = """YES
10001"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()