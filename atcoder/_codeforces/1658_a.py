
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
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        s = input()
        ans = 0
        i = 0
        while i < n:
            #print("turn", i, ans)
            if s[i] == "1":
                i += 1
                continue
            # s[i] == "0"
            if i == n-1:
                i += 1
                continue
            # over 2
            if i + 1 == n-1:
                if s[i+1] == "0": # 00[EOF]
                    ans += 2
                    i += 1
                    continue
                else: #01[EOL
                    i += 1
                    continue
            # over3
            #print("o3")
            if s[i+1] == "0": # 00
                ans += 2
                i += 1
                continue
            else: #01...
                if s[i+2] == "1": #011
                    i += 1
                    continue
                else: #010
                    ans += 1
                    i += 2
                    continue
        print(ans)

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
        input = """9
3
000
3
001
3
010
3
011
3
100
3
101
3
110
3
111
19
1010110000100000101"""
        output = """4
2
1
0
2
0
0
0
17"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """4
1
0
2
00
2
10
2
01"""
        output = """0
2
0
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()