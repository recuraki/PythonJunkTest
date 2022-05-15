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



    def do():
        oh, ow = map(int, input().split())
        maze = []
        for _ in range(oh):
            l = input()
            l = list(l)
            maze.append(l)
        if maze[0][0] == "1":
            print(-1)
            return
        ans = []
        for h in range(oh):
            for w in range(ow):
                if maze[h][w] == "0": continue
                # 1
                hh = h+1
                ww = w+1
                if w != 0:
                    ans.append( (hh, ww - 1, hh, ww) )
                else:
                    ans.append( (hh - 1, ww, hh, ww) )
        print(len(ans))
        for d in reversed(ans):
            print(*d)
        return

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
4 5
01000
10100
01010
00110
2 3
001
010
3 3
110
101
000
1 1
0"""
        output = """4
1 1 3 3
3 3 4 4
4 3 4 4
4 2 4 3
1
1 2 2 3
-1
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()