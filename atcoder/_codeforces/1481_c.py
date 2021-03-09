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
        n, m = map(int, input().split())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        dat3 = list(map(int, input().split()))
        okpaint = collections.defaultdict(list)
        willpaint = collections.defaultdict(list)
        for i in range(n):
            if dat1[i] == dat2[i]:
                okpaint[dat1[i]].append(i)
                continue
            willpaint[dat2[i]].append(i) # color, ind
        #print("-----------------")
        #print(dat3)
        #print("ok", okpaint)
        #print("go", willpaint)
        res = []
        last = -1
        lastind = -1
        for i in range(m):
            x = dat3[i]
            #print("turn",i , "x=", x)
            if len(willpaint[x]) == 0: # not need
                #print(" > no will")
                if len(okpaint[x]) != 0: # not need and can same color
                    #print(" > have ok!")
                    res.append(okpaint[x][0])
                    last = okpaint[x][0]
                    lastind = i
                    continue
                else: # not need and same color is NOT exitst
                    res.append(None)
                    continue
            # need color
            next = willpaint[x].pop()
            res.append(next)
            last = next
            lastind = i
            okpaint[x].append(next)
        #print(res, "lind", lastind, last)
        for i in range(m):
            if res[i] == None:
                if lastind > i:
                    res[i] = last
                else:
                    print("NO")
                    return
        for k in willpaint.keys():
            if len(willpaint[k]) != 0:
                print("NO")
                return
        print("YES")
        print(" ".join(list(map(lambda x: str(x + 1), res))))

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
1 1
1
1
1
5 2
1 2 2 1 1
1 2 2 1 1
1 2
3 3
2 2 2
2 2 2
2 3 2
10 5
7 3 2 1 7 9 4 2 7 9
9 9 2 1 4 9 4 2 3 9
9 9 7 4 3
5 2
1 2 2 1 1
1 2 2 1 1
3 3
6 4
3 4 2 4 1 2
2 3 1 3 1 1
2 2 3 4"""
        output = """YES
1
YES
2 2
YES
1 1 1
YES
2 1 9 5 9
NO
NO"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5 3
1 1 1 1 1
1 2 3 4 5
1 1 1"""
        output = """xxx"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()