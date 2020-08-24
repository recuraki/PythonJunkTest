import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,m,x = map(int, input().split())
    dat = []
    for i in range(n):
        l = list(map(int, input().split()))
        dat.append(l)
    #print(dat)
    res = 999999999999999999999999999
    for i in range(2**n):
        pat = "{:020b}".format(i)
        pat = pat[::-1]
        #print(pat)
        cost = 0
        kekka = [0] * m
        for j in range(n):
            if pat[j] == "1":
                cost += dat[j][0]
                item = dat[j][1:]
                for k in range(m):
                    kekka[k] += item[k]
        can = True
        #print(kekka)
        #print(">cost", cost)
        for k in range(m):
            if kekka[k] < x:
                can= False
        if can:
            #print("ok", cost)
            res = min(res, cost)

    if res == 999999999999999999999999999:
        print(-1)
    else:
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
        input = """3 3 10
60 2 2 4
70 8 7 9
50 2 3 9"""
        output = """120"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 10
100 3 1 4
100 1 5 9
100 2 6 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2"""
        output = """1067"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()