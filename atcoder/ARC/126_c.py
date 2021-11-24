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
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()
        def func(mid):
            need = 0
            for x in dat:
                if x % mid == 0: continue
                need += mid - (x % mid)
            #print("try", mid, need <= k, need, k)
            return need <= k
        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        ok = 0
        ng = INF
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        if func(ok+1): ok = ok + 1
        ook = ok
        while func(ok):
            ok *=2
        ok //= 2
        import math

        candidate = dat[0]
        for x in dat:
            candidate = math.gcd(candidate, x)
        print(max(ok, candidate))

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
        input = """3 6
3 4 9"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4
30 10 20"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 12345
1 2 3 4 5"""
        output = """2472"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()