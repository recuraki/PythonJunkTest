import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    INF = 10**18
    res = INF
    for i in range(q):
        a,p,x = map(int,input().split())
        cur = x - a
        if cur > 0:
            res = min(res, p)
    if res == INF:
        print(-1)
    else:
        print(res)

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
3 9 5
4 8 5
5 7 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
5 9 5
6 8 5
7 7 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
158260522 877914575 602436426
24979445 861648772 623690081
433933447 476190629 262703497
211047202 971407775 628894325
731963982 822804784 450968417
430302156 982631932 161735902
880895728 923078537 707723857
189330739 910286918 802329211
404539679 303238506 317063340
492686568 773361868 125660016"""
        output = """861648772"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()