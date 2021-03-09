import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import math
    def do():
        n, k = map(int, input().split())
        if n == k:
            print(1)
            return
        if n > k:
            if n % k == 0:
                print(1)
                return
            print(2)
            return
        # n < k
        nokori = k - (n % k)
        a = math.ceil(nokori / n)
        #print(n,k,  x, nokori, a)
        print(1 + a)


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
        input = """8
1 5
4 3
8 8
8 17
4 8
4 9
4 7
4 5"""
        output = """5
2
1
3
2
3
2
2"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """8
1 5
4 3
8 8
8 17
4 8
4 9
4 7
4 5"""
        output = """"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()