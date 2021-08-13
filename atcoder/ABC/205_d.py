import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n, q = map(int, input().split())
        dat = list(map(int, input().split()))
        querys = []
        from collections import deque
        masterquerys = []
        for _ in range(q):
            x = int(input())
            querys.append(x)
            masterquerys.append(x)
        querys.sort()
        querys = deque(querys)
        dat.append(0)
        dat.append(10**19)
        dat.sort()
        d = dict()
        start = 1
        for i in range(len(dat)- 1):
            l, r = dat[i], dat[i+1]
            cancount = r - l - 1
            #print(l, r, cancount)
            if cancount == 0:
                continue
            end = start + cancount - 1
            #print("> can make", start, end)
            while len(querys) > 0:
                if start <= querys[0] <= end: # 取れるなら
                    x = querys.popleft()
                    diff = x - start
                    #print(x, "=", l + 1 + diff)
                    d[x] = l + 1 + diff


                else:
                    break

            start = end + 1
        for x in masterquerys:
            print(d[x])



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
        input = """4 3
3 5 6 7
2
5
3"""
        output = """2
9
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2
1 2 3 4 5
1
10"""
        output = """6
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()