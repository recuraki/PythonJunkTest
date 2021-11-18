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
        nokori = n - 1
        done = 1
        time = 0
        while True:
            if nokori <= 0:
                print(time)
                return
            if k < done: break #もし、本数が終わったのより少ないなら、kしかコピーできない
            # k >= done  もし、 k の方が多いなら、doneコピーできる
            nokori -= done
            done += done
            time += 1
        import math
        time += math.ceil(nokori / k)
        print(time)


    # n questions
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
        input = """4
8 3
6 6
7 1
1 1"""
        output = """4
3
6
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()