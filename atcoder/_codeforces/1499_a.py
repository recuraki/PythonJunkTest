
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, a,b = map(int, input().split())
        ww,bb = map(int, input().split())
        total = n
        canwhite = min(a,b)
        #print(">", canwhite)
        canwhite += (max(a,b) - canwhite) // 2
        #print(">", canwhite)
        a,b = n-a, n-b
        canblack = min(a,b)
        canblack += (max(a,b) - canblack) // 2
        #print("--")
        #print(n,a,b,ww,bb)
        #print(canwhite, canblack, ww, bb)
        if canwhite >= ww and canblack >= bb:
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
        input = """5
1 0 1
1 0
1 1 1
0 0
3 0 0
1 3
4 3 1
2 2
5 4 3
3 1"""
        output = """NO
YES
NO
YES
YES"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
1 1 1
1 0
"""
        output = """"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()