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
    from pprint import pprint

    from pprint import pprint

    INF = 1 << 63

    def do():
        n = int(input())
        res = 0
        dat1 = [0] + list(map(int, list(input()))) + [0]
        dat2 = [0] + list(map(int, list(input()))) + [0]

        for i in range(1, n + 1):
            if dat1[i] == 0 and dat2[i] == 1:
                res += 1
                dat1[i] = -1
                dat2[i] = 0

        # print(dat1, dat2)
        for i in range(1, n + 1):
            #print("i", i)
            if dat2[i] == 0: continue
            if dat1[i] == dat1[i + 1] == dat2[i] == dat2[i + 1] == 1:
                #print("pat1")
                dat2[i] = 0
                dat2[i + 1] = 0
                dat1[i] = -1
                dat1[i + 1] = -1
                res += 2
                continue
            if dat2[i - 1] == 1:
                #print("pat2")
                dat1[i] = -1
                dat2[i - 1] = 0
                res += 1
                continue
        for i in range(1, n + 1):
            #print("i", i)
            if dat2[i] == 0: continue
            if dat2[i + 1] == 1:
                #print("pat2")
                dat1[i] = -1
                dat2[i + 1] = 0
                res += 1
                continue

        print(res)

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
3
000
111
4
1111
1111
3
010
010
5
11001
00000"""
        output = """3
4
0
0"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """2
5
01110
11111
4
0110
1111
"""
        output = """4
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()