import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, a, b = map(int, input().split())
    dat_n = []
    # 読み込み
    for i in range(n):
        dat_n.append(int(input()))


    # 隣接３体の合計hp
    dat_hp3 = []
    for i in range(n):
        hp3 = 0
        if i - 1 > 0:
            hp3 += dat_n[i-1]
        hp3 += dat_n[i]
        if i + 1 < n:
            hp3 += dat_n[i+1]
        # 合計hp, 自分のhp, index
        dat_hp3.append((hp3, dat_n[i], i))

    f = True
    count = 0

    if max(dat_hp3) == 0:
        f = False

    while f:
        #print(dat_n)
        #print(dat_hp3)

        dat = sorted(dat_hp3, key = lambda x: (-x[0], -x[1]))
        dat = list(dat)
        # 強さのi
        target = dat[0][2]

        #print("Attack:" + str(target))

        if (target - 1) > 0:
            dat_n[target-1] -= b

        dat_n[target] -= a

        if (target + 1) < n:
            dat_n[target+1] -= b

        # 左右２体のsumを変える
        for i in range(target - 1, target + 2):
            if i  < 0  or i > (n - 1):
                continue

            dat_n[i] = 0 if dat_n[i] < 0 else dat_n[i]

            hp3 = 0
            if i - 1 > 0:
                hp3 += dat_n[i - 1]
            if i  > 0  and i < n:
                hp3 += dat_n[i]
            if i + 1 < n:
                hp3 += dat_n[i + 1]
            # 合計hp, 自分のhp, index
            dat_hp3[i] = (hp3, dat_n[i], i)
            # print("recalc:" + str(i))


        if max(dat_n) == 0:
            break
        count += 1


    print(count - 0)


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
        logging.info("test_input_1")
        input = """4 5 3
8
7
4
2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """2 10 4
20
20"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """5 2 1
900000000
900000000
1000000000
1000000000
1000000000"""
        output = """800000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()