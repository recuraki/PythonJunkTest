import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def solve1(prev, cur):
        # pythonなら間に合いそう
        # retは(足した数, できた数)
        # 前提としてprev > curである
        pstr = str(prev)
        cstr = str(cur)
        plen = len(pstr)
        clen = len(cstr)
        # clenの方が長いことは考えられない。
        #print("solve", prev,cur)
        # plen = clenのとき、0を足すしかない
        #if plen == clen:
        #    res = cstr + "0"
        #    return (1, res)
        #assert prev > cur
        # この時、clenの方がより短い
        if int(pstr[0]) < int(cstr[0]): # 2xxxx vs 3xxxx
            # この場合はおなじまで足せばいい
            saketa = abs(plen - clen)
            res = cstr + ("0" * saketa)
            return (saketa, res)
        if int(pstr[0]) > int(cstr[0]): # 4xxxx vs 3xxxx -> 3xxxx0にするしかない
            # この場合、厳しいので0を桁が上がるまで足す
            saketa = abs(plen - clen) + 1
            res = cstr + ("0" * saketa)
            return (saketa, res)
        # で、これが同じ場合
        # まず確定している文字を確認する
        pheadstr = pstr[:clen]
        #print(pheadstr, "vs", cstr)
        if int(pheadstr) < int(cstr):  # 751 vs 76x
            # この場合、0でpaddingしればよい
            saketa = abs(plen - clen)
            res = cstr + ("0" * saketa)
            return (saketa, res)
        if int(pheadstr) > int(cstr):  # 1040002 103
            #この場合、同じ桁にしても無駄なので1桁あげる
            saketa = abs(plen - clen) +1
            res = cstr + ("0" * saketa)
            return (saketa, res)

        nokori = pstr[plen - (plen - clen):]
        if nokori.count("9") == len(nokori):
            # すべて9の場合は介入の余地がないので1桁あげる
            saketa = abs(plen - clen) + 1
            res = cstr + ("0" * saketa)
            return (saketa, res)

        kekka = list(map(int, list(nokori)))
        for i in range(len(kekka) - 1, -1, -1):
            if kekka[i] != 9:
                kekka[i] += 1
                break

        saketa = abs(plen - clen)
        res = cstr + "".join(list(map(str, kekka)))
        return (saketa, res)

    def do(taskno):
        n = int(input())
        dat = list(map(int, input().split()))
        res = 0
        buf = []
        prevmax = -1
        for i in range(n):
            x = dat[i] # x は current
            if prevmax < x: # すでに条件を満たしているならgo
                prevmax = x
                buf.append(x)
                continue
            else:
                cnt, newx = solve1(prevmax, x)
                newx = int(newx)
                assert newx > prevmax
                res += cnt
                buf.append(newx)
                prevmax = newx
        #print(buf)
        print("Case #{0}: {1}".format(taskno, res))

    q = int(input())
    for qq in range(q):
        do(qq+1)


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
        input = """4
3
100 7 10
2
10 10
3
4 19 1
3
1 2 3"""
        output = """Case #1: 4
Case #2: 1
Case #3: 2
Case #4: 0"""
        #self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
4
123 987654321 987654320 987654320
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()