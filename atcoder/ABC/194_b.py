import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        dat = []
        data = []
        datb = []
        finalres = 10**18
        INF = 10**18
        for _ in range(n):
            a,b = map(int,input().split())
            data.append(a)
            datb.append(b)
        # まずaを最小化
        minvala = min(data)
        candidate = []
        for i in range(n):
            if data[i] == minvala:
                candidate.append(i)
        if len(candidate) > 1:
            minvalb = min(datb)
        else:
            inda = candidate[0]
            minvalb = 10 ** 18
            for i in range(n):
                if i != inda:
                    minvalb = min(minvalb, datb[i])
        #print(minvala, minvalb)
        finalres = min(finalres, max(minvala, minvalb) )

        # まずaを最小化
        minvalb = min(datb)
        candidate = []
        for i in range(n):
            if datb[i] == minvalb:
                candidate.append(i)
        if len(candidate) > 1:
            minvala = min(data)
        else:
            indb = candidate[0]
            minvala = 10 ** 18
            for i in range(n):
                if i != indb:
                    minvala = min(minvala, data[i])

        for i in range(n):
            finalres = min(finalres, data[i] + datb[i])

        #print(minvala, minvalb)
        finalres = min(finalres, max(minvala, minvalb) )

        print(finalres)





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
8 5
4 4
7 9"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
11 7
3 2
6 7"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()