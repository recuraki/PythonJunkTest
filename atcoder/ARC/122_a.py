import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        mod  = 10**9 + 7
        n = int(input())
        dat = list(map(int, input().split()))
        fib = [1, 1, 2, 3]
        p = 2
        pp = 3
        n = n-1
        for i in range(150000):
            fib.append((fib[-2] + fib[-1]) % mod)
        res = []
        res.append(fib[n + 1])
        res.append(fib[n + 0])
        flag = True
        for i in range(n // 2 - 1):
            if flag:
                if (n - 3 - 2 * i) < 0:
                    res.append(res[-1] + 1)
                res.append(res[-1] + fib[n - 3 - 2 * i])
            else:
                if (n - 3 - 2 * i) < 0:
                    res.append(res[-1] - 1)
                res.append(res[-1] - fib[n - 3 - 2 * i])
            flag = not flag
        if n % 2 == 1:
            if (n // 2) % 2 == 0:
                res.append(res[-1] - 1)
            else:
                res.append(res[-1] + 1)
            res.extend(reversed(res[1:-1]))
        else:
            res.extend(reversed(res[1:]))
        rr = 0
        for i in range(n+1):
            rr += dat[i] * res[i]
            rr -= dat[i] * (res[0] - res[i])
            rr %= mod
        print(rr)


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
3 1 5"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1 1 1"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117"""
        output = """279919144"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()