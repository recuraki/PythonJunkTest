import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))

        def f(offset):
            b = dat[0] + offset
            c = -offset
            res = 0
            res += abs(b) + abs(c)
            for x in dat[1:]:
                diff = x - b - c
                if diff == 0:
                    pass
                elif diff > 0:
                    b += diff
                else:
                    c += diff
                res += abs(b) + abs(c)
            return res

        l = -(10 ** 18)
        h = 10 ** 18
        while l <= h:
            mid = (l + h) // 2
            a = f(mid - 1)
            b = f(mid + 0)
            c = f(mid + 1)
            if a == b == c:
                print(a)
                return
            elif a > b:  # 買うことができるなら
                l = mid + 1  # 買えるのでそれ以上の数
            elif b < c:  # 買えないなら
                h = mid - 1  # 買えないのでそれ以下の数をトライ
            else:
                assert False
        res = 10 ** 18
        for i in range(-3, 3):
            res = min(res, f(l + i))
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
1 -2 3"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
5 4 3 5"""
        output = """17"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
-10"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2
1 -1"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()