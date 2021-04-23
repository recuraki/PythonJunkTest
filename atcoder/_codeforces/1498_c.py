import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    memo = dict()
    mod = 10**9 + 7

    def do():
        def sigma1(n):
            return n * (n + 1) // 2
        n, k = map(int, input().split())
        if k == 1:
            print(1)
            return
        if n == 1:
            print(2)
            return
        if n == 2:
            print(k+1)
            return
        res = 2
        kazu = n - 1
        tmp = 0
        for i in range(k):


        res += kazu * tmp
        print(res)



    q = int(input())
    for _ in range(q):
        #print("---")
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
        input = """4
2 3
2 2
3 1
1 3"""
        output = """4
3
1
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1
1 500
500 250"""
        output = """1
2
257950823"""
        self.assertIO(input, output)

    def test_input_22(self):
        print("test_input_22")
        input = """1
4 4"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()