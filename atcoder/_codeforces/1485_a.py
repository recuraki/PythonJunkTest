import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def f(aaa, bbb):
        res = 0
        while aaa // (bbb ** res) != 0:
            res += 1
        return res

    def do():
        a,b  = map(int, input().split())
        #print("----", a,b)
        l = make_divisors(a)
        res = 10**9* 2
        prev = 10**9* 2+1
        new = 10**9* 2
        offset = 0
        while True:
            x = b + offset
            offset += 1
            if x == 1:
                continue
            cnt = x - b
            cnt += f(a, x)
            res = min(res, cnt)
            if prev < cnt:
                break
            prev = cnt
        print(res)



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
        input = """6
9 2
1337 1
1 1
50000000 4
991026972 997
1234 5678"""
        output = """4
9
2
12
3
1"""
        self.assertIO(input, output)

    def test_input_12(self):
        print("test_input_12")
        input = """1
10 1"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()