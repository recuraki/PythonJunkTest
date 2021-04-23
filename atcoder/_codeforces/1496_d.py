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
        n = int(input())
        dat = list(map(int, input().split()))
        # a turn
        stepa = [0] * n
        stepb = [0] * n
        stepc = [0] * n
        stepd = [0] * n
        for i in range(1, n):
            if dat[i] > dat[i - 1]:
                stepa[i] = stepa[i-1] + 1
            if dat[i] < dat[i - 1]:
                stepb[i] = stepb[i-1] + 1
        for i in range(n-1-1, -1, -1):
            if dat[i] > dat[i + 1]:
                stepc[i] = stepc[i+1] + 1
            if dat[i] < dat[i + 1]:
                stepd[i] = stepd[i+1] + 1
        data = [0] * n
        datb = [0] * n
        for i in range(n):
            data[i] = max(stepa[i], stepc[i])
            datb[i] = max(stepb[i], stepd[i])

        maxval = max(data)
        # odddddddddddddd
        if maxval % 2 == 1:
            print(0)
            return
        # even
        #print(data)
        #print(datb)
        ret = 0
        cnt = datb.count(maxval)
        if cnt == 1 or cnt == 2 or True:
            print(1)
            return
        print(0)



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
        input = """5
1 2 5 4 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
1 2 4 6 5 3 7"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1 2 8 6 5 3 4 7 9 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """11
1 4 6 8  10 11 9 7 5 3 2"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()