import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    from pprint import pprint
    from collections import deque
    def do():
        s = input()
        n = len(s)
        q = deque(list(s))
        can = True
        for i in range(n):
            predict = chr( ord("a") + n -1 - i)
            #print(predict)
            if q[0] == predict:
                q.popleft()
                continue
            if q[-1] == predict:
                q.pop()
                continue
            can = False
            break
        if can:
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
        input = """11
a
ba
ab
bac
ihfcbadeg
z
aa
ca
acb
xyz
ddcba"""
        output = """YES
YES
YES
YES
YES
NO
NO
NO
NO
NO
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()