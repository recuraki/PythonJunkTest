import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def resolve():
    # input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        dat = []
        maxwalk = 0
        maxgoto = 0
        for i in range(n):
            if data[i] <= datb[i]:  # goto eat is fast then skip
                maxgoto = max(maxgoto, data[i])
                continue
            maxwalk += datb[i]
            dat.append([data[i], datb[i], data[i] - datb[i]])
        dat.sort(key=lambda x: (x[0]), reverse=True)
        #print(dat)

        maxwalk = 0
        for i in range(len(dat)):
            a, b, d = dat[i]
            tmpwalk = maxwalk + b
            tmpgoto = a
            if tmpwalk <= tmpgoto:
                maxwalk += b
            else:
                maxgoto = tmpgoto
                break
        print(max(maxwalk, maxgoto))

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
        input = """4
4
3 7 4 5
2 1 2 4
4
1 2 3 4
3 3 3 3
2
1 2
10 10
2
10 10
1 2"""
        output = """5
3
2
3"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """6
4
4 4 4 4
4 4 4 4
4
2 2 10 10
2 10 2 10
3
2 2 10
2 10 2
3
3 3 3
2 2 2
3
10000 7 7
2 4 2
3
2 7 7
10000 4 2"""
        output = """4
10
2
3
7
6"""
        self.assertIO(input, output)


    def test_input_111(self):
        print("test_input_111")
        input = """1
1
10 2
1  10"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()