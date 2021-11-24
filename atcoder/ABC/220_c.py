import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63

    def do():
        import math
        res = 0
        n = int(input())
        dat = list(map(int, input().split()))
        kai = sum(dat) # 合計
        x = int(input())
        loop = x // kai # 何回回る
        res += loop * n
        x %= kai
        for i in range(n):
            if x < 0: break
            res += 1
            x -= dat[i]
            if x < 0: break
        print(res)



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
3 5 2
26"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
12 34 56 78
1000"""
        output = """23"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()