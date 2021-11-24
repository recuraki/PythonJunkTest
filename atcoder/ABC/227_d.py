import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        total = sum(dat)
        def func(mid): # midグループ作れるかの判定
            # k種類作れればOK
            compk = 0
            curkneed = mid # そのkを作るにはあとこの人数必要です
            if mid > total: return False
            for i in range(n):
                if compk == k: return True
                curdept = dat[i] # 今の部署の人数
                if curkneed <= curdept: # もし、今作りたいグループに人が足りているなら
                    compk += 1
                    curdept -= curkneed
                    used = curkneed # kneed人は使ったので、
                    curkneed = mid # 本来、次、mid人充てるんだけど
                    # もし、「今の部署に当てたグループ」以外に充てられるならその分は充てる。
                    curkneed -= min(curdept, curkneed - used)
                    if compk == k: return True
                    continue
                # 今作りたいグループにこの部署を全員充てる
                curkneed -= curdept
            return False
        ok = 0
        ng = 10 ** 20 + 10
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        print(ok)
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
        input = """3 3
2 3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 2
1 1 3 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 3
1 1 3 4"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()