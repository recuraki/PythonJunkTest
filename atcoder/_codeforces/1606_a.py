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



    import math
    INF = 1 << 63
    def do():
        s = input()
        l = list(s)
        def ab(x):
            cnt = 0
            for i in range(len(x) - 1):
                if x[i] == "a" and x[i+1] == "b": cnt += 1
            return cnt
        def ba(x):
            cnt = 0
            for i in range(len(x) - 1):
                if x[i] == "b" and x[i+1] == "a": cnt += 1
            return cnt
        if ab(s) == ba(s):
            print(s)
            return
        for i in [0, -1]:
            orig = l[i]
            if orig == "a": l[i] = "b"
            elif orig == "b": l[i] = "a"
            if ab(l) == ba(l):
                print("".join(l))
                return
            l[i] = orig
        assert False


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
b
aabbbabaa
abbb
abbaab"""
        output = """b
aabbbabaa
bbbb
abbaaa"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()