import sys
from io import StringIO
import unittest


import sys
sys.setrecursionlimit(2000000)
def do_action(q, temoto, value, k_remain):
    if k_remain == 0:
        return value
    a = b = c = d = e = -100000000

    # どっちを掘るか決める
    l_sum = r_sum = 0
    for i in range(min(k_remain, len(q))):
        if q[i] > 0:
            l_sum += q[i]
        if q[- (i + 1)] > 0:
            r_sum += q[- (i + 1)]

    # a
    if l_sum >= r_sum and l_sum > 0:
        if len(q) != 0:
            val = q[0]
            a = do_action(q[1:], temoto + [val], value + val, k_remain - 1)
    # b
    if r_sum <= l_sum and r_sum > 0:
        if len(q) != 0:
            val = q[-1]
            b = do_action(q[:-1], temoto + [val], value + val, k_remain - 1)

    temoto.sort()
    # 戻す可能性があるのは負のがあるときのみ
    if len(temoto) > 0 and temoto[0] < 0:
        # c
        if len(temoto) != 0:
            temoto.sort()
            val = temoto[0]
            c = do_action([val] + q , temoto[1:], value - val, k_remain - 1)
        # d
        if len(temoto) != 0:
            temoto.sort()
            val = temoto[0]
            d = do_action(q + [val], temoto[1:], value - val, k_remain - 1)
    # e
    e = do_action(q , temoto, value, k_remain - 1)

    return max(a,b,c,d,e)

def resolve():
    n, k = map(int, input().split())
    dat_v = map(int, input().split())
    dat_v = list(dat_v)
    val = do_action(dat_v, [], 0, k)
    print(val)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test__1(self):
        input = """6 4
-10 8 2 1 2 6"""
        output = """14"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 3
-6 -100 50 -2 -5 -3"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()