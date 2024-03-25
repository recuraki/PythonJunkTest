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
        n = int(input())
        datx = list(map(lambda x: int(x) - 1, input().split()))
        datc = list(map(int, input().split()))
        buf = [0] * n
        for i in range(n):
            buf[datx[i]] += datc[i]
        #print(buf)
        tmp = []
        for i in range(n):
            tmp.append( (buf[i], i) )
        tmp.sort()
        #print(tmp)
        visited = [False] * n
        ans = 0
        for cost, ind in tmp:
            if visited[datx[ind]]: ans += datc[ind]
            visited[ind] = True
        print(ans)

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
2 3 2
1 10 100"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8
7 3 5 5 8 4 1 2
36 49 73 38 30 85 27 45"""
        output = """57"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()