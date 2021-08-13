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
    def do():
        n, k = map(int, input().split())
        s = input()
        res = []
        for base in range(0, n):
            ll = []
            for i in range(k):
                ll.append(s[i % (base+1)])
            res.append("".join(ll))
            print(ll)
        res.sort()

        #pprint(res)
        print(res[0])


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
        input = """8 16
dbcadabc"""
        output = """dbcadabcdbcadabc"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 5
abcd"""
        output = """aaaaa"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()