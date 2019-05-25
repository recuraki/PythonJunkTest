import sys
from io import StringIO
import unittest

def resolve():
    n,m = map(int, input().split())
    dat_a = map(int, input().split())
    dat_a = list(dat_a)
    dat_a.sort()
    trade = []
    for i in range(m):
        b, c = map(int, input().split())
        trade.append((b,c))
    trade.sort(key=lambda x: -x[1])

    cur_remain = 0
    cur_num = 0
    cur = -1
    for i in range(n):
        if cur_remain == 0:
            cur += 1
            if cur >= len(trade):
                break
            cur_remain = trade[cur][0]
            cur_num = trade[cur][1]
        if dat_a[i] < cur_num:
            cur_remain -= 1
            dat_a[i] = cur_num
        else:
            break
    print(sum(dat_a))






class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()