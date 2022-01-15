import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys, math
    input = sys.stdin.readline
    INF = 1 << 63
    def do():
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        def func(mid): # mid枚で払えますか？
            used = 0
            nokori = x
            for i in range(n-1, -1, -1):
                used += nokori // dat[i]
                nokori %= dat[i]
            if used <= mid: return True
            return False

        ng = 0
        ok = 10 ** 18 + 10
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        ans = ok # candidate
        print(ans)
        for z in range(1):
            for i in range(n): # 1枚目を使ってみるとする
                cur = dat[i] # これを使う
                firstneed = math.ceil(x / cur) + z
                used = firstneed
                nokori = (firstneed * cur) - x
                print("use yen", cur, "maisuu", firstneed, "nokori", nokori)
                # この場合のおつりは？
                for j in range(n-1, -1, -1):
                    used += nokori // dat[j]
                    nokori %= dat[j]
                print(i, used)
                ans = min(ans, used)
        print(ans)

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
        input = """3 87
1 10 100"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 49
1 7"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000"""
        output = """233"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()