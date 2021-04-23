import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    # 素因数分解
    """
    >>> factorization(16)
    [[2, 4]]
    >>> factorization(48)
    [[2, 4], [3, 1]]
    """

    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    # [2, 5, 5]
    def factorization_expand(n):
        l = factorization(n)
        dat = []
        for a, b in l:
            dat += [a] * b
        return dat

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        import collections
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        ss = set()
        res = 1
        for x in dat:
            l = factorization_expand(x)
            for xx in l:
                if xx in ss:
                    ss.remove(xx)
                else: # not in
                    ss.add(xx)
            if len


    q = int(input())
    for _ in range(q):
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
        input = """3
5 0
18 6 2 4 1
5 0
6 8 1 24 8
1 0
1"""
        output = """3
2
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()