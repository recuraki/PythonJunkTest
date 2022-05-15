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
        from collections import deque
        question = int(input())
        dat = deque([])
        for _ in range(question):
            query = list(map(int, input().split()))
            if query[0] == 1:
                x, c = query[1:]
                dat.append( (x, c) )
            elif query[0] == 2:
                c = query[1]
                ans = 0
                while c > 0:
                    x, cnt = dat.popleft()
                    can = min(c, cnt)
                    ans += x * can # 消せるだけ消す
                    cnt -= can
                    c -= can
                    if cnt == 0: continue
                    dat.appendleft( (x, cnt) )

                print(ans)
            else:
                assert False

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
1 2 3
2 2
1 3 4
2 3"""
        output = """4
8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1 1000000000 1000000000
2 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()