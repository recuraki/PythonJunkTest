import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    C = collections.Counter(dat)
    res = 0
    i = 0
    #print(C)
    ccc = 0
    while True:
        if i in C:
            val = C[i]
        else:
            val = 0
        can = min(val, k)
        tarinai = k - can
        if tarinai != 0:
            res += i * tarinai
        k = k - tarinai
        if can == 0:
            break
        i+=1
    print(res)




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
        input = """4 2
0 1 0 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2
0 1 1 2 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0"""
        output = """11"""
        self.assertIO(input, output)




if __name__ == "__main__":
    unittest.main()