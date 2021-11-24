import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
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
        n, m = map(int, input().split())
        dat = list(map(int, input().split()))
        ss = set()
        tt = set(range(1, m+1))

        for x in dat:
            l = factorization(x)
            for p, _ in l:
                ss.add(p)

        if 1 in ss: ss.remove(1)

        for x in ss:
            i = 1
            while (x*i) <= m:
                if (x*i) in tt: tt.remove(x*i)
                i += 1

        tt.add(1)
        tt = list(tt)
        print(len(tt))
        for x in tt: print(x)
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
        input = """3 12
6 1 5"""
        output = """3
1
7
11"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()