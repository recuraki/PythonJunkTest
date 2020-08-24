import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def do():
        l = 0
        r = 10**9 + 1
        while l <= r:
            mid = (l+r) // 2
            if do2(mid) is True: # 作れるなら
                r = mid - 1
            else:
                l = mid + 1
        return l

    def do2(target):
        res = 0
        if target == 0:
            return False
        t = math.log(target, 2)
        kk = k
        for i in range(n):
            if target >= dat[i]:
                break
            kk -= math.ceil(dat[i] / target) - 1
            if kk < 0:
                return False
        return True

    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    dat.sort(reverse=True)
    print(do())


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
        input = """2 3
7 9"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 0
3 4 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202"""
        output = """292638192"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()