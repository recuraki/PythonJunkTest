import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    def do():
        import random
        def is_prime(q, k=50):
            q = abs(q)
            if q == 2: return True
            if q < 2 or q & 1 == 0: return False

            d = (q - 1) >> 1
            while d & 1 == 0:
                d >>= 1

            for i in range(k):
                a = random.randint(1, q - 1)
                t = d
                y = pow(a, t, q)
                while t != q - 1 and y != 1 and y != q - 1:
                    y = pow(y, 2, q)
                    t <<= 1
                if y != q - 1 and t & 1 == 0:
                    return False
            return True

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

        n = int(input())

        if is_prime(n):
            res = list(range(1, 1 + n))
        else:
            res = set(range(1, 1 + n))
            l = factorization(n)
            for x, cnt in l:
                i = 1
                while (i * x) <= n:
                    if (i * x) in res:
                        res.remove(i * x)
                    i += 1

        res = list(res)
        res.sort()
        while True:
            val = 1
            for x in res:
                val *= x
                val %= n
            if val == 1:
                break
            del res[-1]
        print(len(res))
        print(" ".join(list(map(str, res))))
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
        input = """5"""
        output = """3
1 2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8"""
        output = """4
1 3 5 7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2"""
        output = """1
1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """999983"""
        output = """1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()