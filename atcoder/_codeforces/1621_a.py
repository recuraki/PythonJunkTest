import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n, k = map(int, input().split())
        if n % 2 == 0:  # even
            if (n // 2) < k:
                print(-1)
                return
        else:
            if ((n+1) // 2) < k:
                print(-1)
                return
        for h in range(n):
            if h % 2 == 1:
                print("." * n)
                continue
            else:
                if k == 0:
                    print("." * n)
                    continue
                else:
                    k -= 1
                    l = ["."] * n
                    l[k * 2] = "R"
                    print("".join(l))

                    # n questions
    q = int(input())
    for _ in range(q):
        do()
    # 1 time







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
3 2
3 3
1 1
5 2
40 33"""
        output = """..R
...
R..
-1
R
.....
R....
.....
....R
.....
-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()