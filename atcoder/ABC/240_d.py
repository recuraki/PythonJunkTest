import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        from collections import deque
        q = deque([])
        ans = 0
        for x in dat:

            if len(q) == 0: # 空なら2つだけ淹れる
                q.append( (x, 1) )
                ans += 1
                print(ans)
                continue
            col, num = q.pop()
            if col != x:
                ans += 1
                print(ans)
                q.append( (col, num) )
                q.append( (x, 1) )
            else: # same color!
                ans -= num
                num += 1
                if num == x:
                    pass
                else:
                    ans += num
                    q.append((col, num))
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
        input = """5
3 2 3 2 2"""
        output = """1
2
3
4
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
2 3 2 3 3 3 2 3 3 2"""
        output = """1
2
3
4
5
3
2
3
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()