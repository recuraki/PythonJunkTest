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

    INF = 1 << 63

    issqrt = set()
    for i in range(0, 1000000):
        issqrt.add(str(2 ** i))
        if (2**i) > 10**24:
            break
    def do():
        n = int(input())
        s = str(n)
        sl = len(s)
        res = 10 ** 9
        if s in issqrt:
            print(0)
            return
        for candidate in issqrt:
            found = 0
            for i in range(len(s)):
                if s[i] == candidate[found]:
                    found += 1
                if found == len(candidate): break
            need = 0
            need += sl - found # need erase
            need += len(candidate) - found # must add
            res = min(res, need)

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
        input = """12
1052
8888
6
75
128
1
301
12048
1504
6656
1000000000
687194767"""
        output = """2
3
1
3
0
0
2
1
3
4
9
2"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """5
1
2
4
8
7
"""
        output = """2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()