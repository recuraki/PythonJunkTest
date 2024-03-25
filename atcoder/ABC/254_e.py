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
        n, m = map(int, input().split())
        link = [list() for _ in range(n)]
        g = [[set() for _ in range(n)] for _ in range(4)]
        for i in range(n):
            g[0][i].add(i)
            g[1][i].add(i)
        for _ in range(m):
            a, b = map(int, input().split())
            a-=1
            b-=1
            g[1][a].add(b)
            g[1][b].add(a)
            link[a].append(b)
            link[b].append(a)
        for i in range(n):
            for x in g[1][i]: g[2][i].add(x)
            for nxt in link[i]:
                for x in g[1][nxt]: g[2][i].add(x)

        for i in range(n):
            for x in g[2][i]: g[3][i].add(x)
            for nxt in g[2][i]:
                for x in g[1][nxt]: g[3][i].add(x)


        q = int(input())
        #print(g)
        for _ in range(q):
            x, k = map(int, input().split())
            x -= 1
            ans = 0
            for y in g[k][x]:
                ans += y+1
            print(ans)


    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3"""
        output = """1
20
2
20
7
6
20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()