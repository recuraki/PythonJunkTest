import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        # エトラステネスのふるい
        #  https://qiita.com/fantm21/items/5e270dce9f4f1d963c1e
        """
        nまでの素数を一覧する。(nを含む)
        >> prime_list_eratosthenes(9)
        [2, 3, 5, 7, 9]
        """

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

        """
        n_from以上、n_to以下の素数を一覧する。(fromとtoを含む = [from, to]
        >> prime_list_eratosthenes_from(5,9)
        [5, 7, 9]
        """

        def prime_list_eratosthenes_from(n_from, n_to):
            from bisect import bisect_left
            data = prime_list_eratosthenes(n_to)
            i = bisect_left(data, n_from)
            return data[i:]

        ps = prime_list_eratosthenes(1000)
        a, b, c, d = map(int, input().split())
        for i in range(a, b+1):
            canWin = True
            for j in range(c, d+1):
                x = i + j
                if x in ps: canWin = False
            if canWin:
                print("Takahashi")
                return
        print("Aoki")
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
        input = """2 3 3 4"""
        output = """Aoki"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 100 50 60"""
        output = """Takahashi"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 14 1 5"""
        output = """Aoki"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()