import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        import math
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        datmax = max(dat)
        ss = set(dat)
        #print(ss)
        datmex = 0
        while datmex in ss:
            datmex+= 1

        for i in range(k):
            #print(i,datmex,datmax)
            if datmex == (datmax + 1):
                print(len(ss) + (k-i))
                return
            x = math.ceil( (datmax + datmex) / 2)
            datmax = max(datmax, x)
            if x in ss:
                break
            ss.add(x)
            while datmex in ss:
                datmex += 1
        #print(ss)
        print(len(ss))


    q = int(input())
    for _ in range(q):
        do()
    # do()



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
        input = """5
4 1
0 1 3 4
3 1
0 1 4
3 0
0 1 4
3 2
0 1 2
3 2
1 2 3"""
        output = """4
4
3
5
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5 100
0 10 2 3 100"""
        output = """13"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()