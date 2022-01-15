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
    from pprint import pprint
    import math
    INF = 1 << 63
    def do():
        n = int(input())
        s = input()
        if n == 1:
            print(s[0]*2)
            return
        dat = [s[0] * 2]
        for i in range(1, n):
            if ord(s[i-1]) >= ord(s[i]): continue
            i -= 1
            break
        dat.append(s[:i+1] + s[:i+1][::-1])
        i+=1
        if i+1 != n:
            dat.append(s[:i+1] + s[:i+1][::-1])
        dat.sort()
        print(dat[0])



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
10
codeforces
9
cbacbacba
3
aaa
4
bbaa"""
        output = """cc
cbaabc
aa
bb"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
1
d"""
        output = """dd"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()