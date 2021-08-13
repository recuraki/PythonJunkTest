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
        dat = [0] + list(map(int, input().split()))
        res = 0
        for i in range(1, n + 1):
            #print(">>>> gogo i = ", i)
            x = dat[i]
            cnt = 1
            #print(x*cnt, n)
            while True:
                targetval = x * cnt
                #print("target", targetval)
                nextind = targetval - i
                #print("try", i, nextind)
                if nextind <= i:
                    cnt += 1
                    continue
                if n < nextind: break
                if x * dat[nextind] == targetval:
                    #print(i, nextind, "val", targetval)
                    res += 1
                cnt += 1
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
2
3 1
3
6 1 5
5
3 1 5 9 2"""
        output = """1
1
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()