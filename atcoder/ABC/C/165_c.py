import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m, q = map(int, input().split())
    cond = []

    for qq in range(q):
        a,b,c,d = map(int, input().split())
        cond.append([a,b,c,d])

    cond.sort()
    #print(cond)
    finalres = 0
    dat = [1] * n
    while True:
        for i in range(n - 1, -1, -1):
            if dat[i] > m:
                dat[i] = dat[i - 1]
                dat[i - 1] += 1
            else:
                break
        ispass = False
        for i in range(n - 1, 0, -1):
            if dat[i] < dat[i - 1]:
                ispass = True
                break
        if ispass:
            dat[n - 1] += 1
            if dat[0] >= m:
                break
            continue

        #print("Try:", dat)

        can = True
        res = 0
        for i in range(q):
            a, b, c, d = cond[i]
            a, b = a-1, b-1
            if dat[b] - dat[a] == c:
                #print(" > match i{0} -i{1} == c gain {2}".format(b, a, d))
                res += d
        finalres = max(finalres, res)

        dat[n - 1] += 1
        if dat[0] >= m:
            break
    print(finalres)




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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_13(self):
        print("test_input_3")
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()