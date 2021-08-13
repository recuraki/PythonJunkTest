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
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        d0 = dat[0]
        s0 = "{:032b}".format(d0)
        res = [0]
        for i in range(1, n):
            d = dat[i]
            s = "{:032b}".format(d)
            tmp = ""
            for k in range(32):
                if s0[k] == "1" and s[k] == "0":
                    tmp += "1"
                else:
                    tmp += "0"
            #print(tmp)
            res.append(int(tmp, 2))
            d0 |= d
            s0 = "{:032b}".format(d0)

        print(" ".join(list(map(str, res))))

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
        input = """5
4
1 3 7 15
4
1 2 4 8
5
1 2 3 4 5
4
11 13 15 1
1
0"""
        output = """0 0 0 0
0 1 3 7
0 1 0 3 2
0 2 0 14
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()