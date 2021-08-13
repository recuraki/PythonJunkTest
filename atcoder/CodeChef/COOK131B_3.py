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


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        from collections import Counter, defaultdict
        n = int(input())
        dat = list(map(int, input().split()))
        d = defaultdict(int)
        for x in dat:d[x] += 1
        #buf = []
        res = 0
        for key in d.keys():
            #buf.append( (key, d[key]) )
            res += min(key-1, d[key])
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
        input = """3
6
2 2 4 4 2 6 
2
16 8
2
2 3"""
        output = """4
2
2
"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()