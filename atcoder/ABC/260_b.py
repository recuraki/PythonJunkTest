import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, x, y, z = map(int, input().split())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        ans = []
        buf = []
        visited = [False] * n

        for i in range(n):
            a = data[i]
            b = datb[i]
            buf.append( (a, -i ) )
        ok = 0
        buf.sort(reverse=True)
        for i in range(n):
            if ok == x: break
            _, ind = buf[i]
            ind = -ind
            if visited[ind]: continue
            visited[ind] = True
            ans.append(ind)
            ok += 1


        buf = []
        for i in range(n):
            a = data[i]
            b = datb[i]
            buf.append( (b, -i ) )
        ok = 0
        buf.sort(reverse=True)
        for i in range(n):
            if ok == y: break
            _, ind = buf[i]
            ind = -ind
            if visited[ind]: continue
            visited[ind] = True
            ans.append(ind)
            ok += 1


        buf = []
        for i in range(n):
            a = data[i]
            b = datb[i]
            buf.append( (a+b, -i ) )
        ok = 0
        buf.sort(reverse=True)

        for i in range(n):
            if ok == z: break
            _, ind = buf[i]
            ind = -ind
            if visited[ind]: continue
            visited[ind] = True
            ans.append(ind)
            ok += 1

        ans.sort()
        for x in ans: print(x+1)



    # 1 time
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
        input = """6 1 0 2
80 60 80 60 70 70
40 20 50 90 90 80"""
        output = """1
4
5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2 1 2
0 100 0 100 0
0 0 100 100 0"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """15 4 3 2
30 65 20 95 100 45 70 85 20 35 95 50 40 15 85
0 25 45 35 65 70 80 90 40 55 20 20 45 75 100"""
        output = """2
4
5
6
7
8
11
14
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()