import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        n = int(input())
        dat = list(map(lambda x: int(x)-1, input().split()))
        import collections
        c = collections.Counter(dat)
        buf = []
        for k in c:
            buf.append([k, c[k]])
        buf.sort(reverse=True)
        #print(buf)
        dat = []
        for num, cnt in buf:
            for _ in range(cnt):
                dat.append(num)
        dat.sort()
        #print(dat)
        used = [False] * 400
        cost = 0
        for i in range(n):
            xxx = dat[i]
            #print(i, used[:10], cost)
            for j in range(200):
                if (xxx-j) >= 0 and used[xxx - j] is False:
                    used[xxx - j] = True
                    cost += j
                    break
                if (xxx+j) <= (399)  and used[xxx + j] is False:
                    used[xxx + j] = True
                    cost += j
                    break
        print(cost)
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
6
4 2 4 4 5 2
7
7 7 7 7 7 7 7
1
1
5
5 1 2 4 3
4
1 4 4 4
21
21 8 1 4 1 5 21 1 8 21 11 21 11 3 12 8 19 15 9 11 13"""
        output = """4
12
0
0
2
21"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()