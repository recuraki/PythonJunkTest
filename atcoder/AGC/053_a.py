import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from copy import deepcopy
    def isok(num):
        if num > maxval:
            return False, None
        l = []
        for i in range(n+1):
            l.append(dat[i] // num)
        res = []
        for i in range(num):
            res.append(deepcopy(l))
        for i in range(n+1):
            for j in range(dat[i] % num):
                res[j][i] += 1
        calc = [0] * (n+1)
        for l in res:
            for i in range(n+1):
                calc[i] += l[i]
        for i in range(num):
            if not isoklist(res[i]):
                return False, None
        return True, res

    def isoklist(l):
        #print("isok?", l)
        can = True
        for i in range(n):
            x, y = l[i], l[i + 1]
            if s[i] == ">":
                if x > y:
                    continue
                can = False
                break
            elif s[i] == "<":
                if x < y:
                    continue
                can = False
                break
            else:
                assert False
        return can

    from pprint import pprint
    from copy import deepcopy
    n = int(input())
    s = input()
    prevdat = None
    res = []
    dat = list(map(int, input().split()))

    maxval = max(dat)
    l = 1
    h = 1000000000
    while l <= h:
        mid = (l + h) // 2
        #print("try", mid)
        flag, res = isok(mid)
        if flag:  # 買うことができるなら
            l = mid + 1  # 買えるのでそれ以上の数
        else:  # 買えないなら
            h = mid - 1  # 買えないのでそれ以下の数をトライ
    flag, res = isok(h)
    if flag is False:
        flag, res = isok(l)

    print(len(res))
    for i in range(len(res)):
        print(" ".join(list(map(str, res[i]))))





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
<><
3 8 6 10"""
        output = """2
1 5 4 7
2 3 2 3"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """3
<><
3 10 4 10"""
        output = """"""
        self.assertIO(input, output)

    def test_input_123(self):
        print("test_input_123")
        input = """3
<><
0 1 0 1"""
        output = """"""
        self.assertIO(input, output)

    def test_input_123(self):
        print("test_input_123")
        input = """3
<><
0 3 0 2"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()