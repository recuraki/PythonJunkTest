import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))
        cnttarget = dat.count(x)
        if n == cnttarget:
            print("NO")
            return
        if sum(dat) == x:
            print("NO")
            return
        visited = [False] * n
        s = 0
        res = []
        while True:
            if s == sum(dat):
                break
            used = False
            for i in range(n):
                if visited[i]:
                    continue
                if (s + dat[i]) != x:
                    s += dat[i]
                    visited[i] = True
                    res.append(dat[i])
                    used = True
            if used is False:
                print("NO")
                return

        print("YES")
        print(" ".join(list(map(str, res))))

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
3 2
3 2 1
5 3
1 2 3 4 8
1 5
5"""
        output = """YES
3 2 1
YES
8 1 2 3 4
NO"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1
3 6
2 2 2
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()