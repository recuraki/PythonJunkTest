import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63

    def prime_list_eratosthenes(n):
        import math
        if n == 1:
            return []
        if n == 2:
            return [2]
        prime = [2]
        limit = math.sqrt(n)
        data = [i + 1 for i in range(2, n, 2)]
        while True:
            p = data[0]
            if limit < p:
                return prime + data
            prime.append(p)
            data = [e for e in data if e % p != 0]
    def prime_list_eratosthenes_from(n_from, n_to):
        from bisect import bisect_left
        data = prime_list_eratosthenes(n_to)
        i = bisect_left(data, n_from)
        return data[i:]
    dat = prime_list_eratosthenes_from(1, 200000)

    def do():
        n = int(input())
        print(" ".join(list(map(str, dat[1:1+n]))))

    # n questions
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
1
2
1000"""
        output = """1
2 3
111 1111 11111 111111 1111111 11111111 111111111"""
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
        self.assertIO(input
                      , output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()