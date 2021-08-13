import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        print(sum(data), sum(datb))
        import collections
        suma = 0
        sumb = 0
        diff = 0
        for i in range(n):
            suma += data[i] + i
            sumb += datb[i] + i
            x =  (data[i] - datb[i])
            if x < 0:
                diff += x
        print(suma, sumb, diff)




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
3 1 4
6 2 0"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1 1
1 1 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
5 4 1 3 2
5 4 1 3 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6
8 5 4 7 4 5
10 5 6 7 4 1"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()