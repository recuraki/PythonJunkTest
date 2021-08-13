import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import fractions
    def lcm(x, y):
        return (x * y) // fractions.gcd(x, y)

    import math
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

    # input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        s = sum(dat)
        res = []
        cur = dat[0]
        # print(dat)
        for i in range(n):
            v = math.floor(math.log2(dat[i]))
            x, y = (2 ** v, 2 ** (v + 1))
            if abs(dat[i] - x) < abs(dat[i] - y):
                res.append(x)
            else:
                if y > 10**9:
                    res.append(y//2)
                else:
                    res.append(y)

        t = 0
        for i in range(n):
            t += abs(dat[i] - res[i])
        # print(2*t, "<=", s)
        # print(2*t <= s)

        print(" ".join(list(map(str, res))))

    q = int(input())
    for _ in range(q):
        do()
    # do()


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
        input = """5
5
1 1 3 1 1
2
4 6
2
1 1000000000
6
3 4 8 1 2 3
6
1 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """3 3 3 3 3
3 6
1 1000000000
4 4 8 1 3 3
-"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()