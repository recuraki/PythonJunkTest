
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def BubbleSort(num):
        num = list(num)
        nocnt = 0

        num = list(map(lambda x: x - 1, num))

        s = set(num)
        for i in range(len(num)):
            if i not in s:
                nocnt += 1

        pos = [-1] * len(num)
        cnt = 0
        for i in range(len(num)):
            pos[num[i]] = i
        for i in range(len(num)):
            if i not in s:
                continue
            if num[i] == i:
                continue
            dummynum = num[i]
            pos[dummynum] = pos[i]  # ここにいるのを本来の数に飛ばす
            num[pos[i]] = dummynum
            cnt += 1
        return cnt + nocnt

    mod = 998244353
    n = int(input())
    dat = list(map(int, input().split()))
    cnt = BubbleSort(dat)
    #print(dat, cnt)
    x = n - cnt
    res = pow(2, x, mod) - 1
    if res < 1:
        res = 1
    print(res % mod)

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
        input = """2
2 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1 2 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """5
2 3 4 5 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_311(self):
        print("test_input_311")
        input = """5
1 5 2 3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3111(self):
        print("test_input_3111")
        input = """5
2 1 4 3 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_311111(self):
        print("test_input_311111")
        input = """5
1 4 3 2 5"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_31111(self):
        print("test_input_31111")
        input = """5
1 2 3 4 5"""
        output = """31"""
        self.assertIO(input, output)

    def test_input_311111(self):
        print("test_input_311111")
        input = """5
1 2 3 4 5"""
        output = """31"""
        self.assertIO(input, output)
    def test_input_311211(self):
        print("test_input_311211")
        input = """4
4 2 3 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_3112111(self):
        print("test_input_3111211")
        input = """4
4 2 4 3"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()