import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    dat_r = []
    dat_b = []

    n = int(input())
    for i in range(n):
        a,b = map(int, input().split())
        dat_r.append((a, b))

    for i in range(n):
        c,d = map(int, input().split())
        dat_b.append((c, d))

    dat_r.sort(key=lambda x: ( -x[1], -x[0]-x[1]))
    dat_b.sort(key=lambda x: ( +x[0],  x[0]+x[1]))
    #print("")
    #print(dat_r)
    #print(dat_b)
    res = 0
    """
    for i in range(n):
        for j in range(len(dat_b)):
            # print("{0} < {1} vs {2} < {3}".format(dat_r[i][0] ,dat_b[j][0] ,dat_r[i][1] ,dat_b[j][1]))
            if dat_r[i][0] < dat_b[j][0] and dat_r[i][1] < dat_b[j][1]:
                # print("ok")
                res += 1
                dat_b  = dat_b[0:j] + dat_b[j + 1:]
                break
    print(res)
    """
    for i in range(n):
        for j in range(len(dat_r)):
            #print("{0} < {1} vs {2} < {3}".format(dat_r[i][0] ,dat_b[j][0] ,dat_r[i][1] ,dat_b[j][1]))
            if dat_r[j][0] < dat_b[i][0] and dat_r[j][1] < dat_b[i][1]:
                #print("ok")
                res += 1
                dat_r  = dat_r[0:j] + dat_r[j + 1:]
                break
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
        logging.info("test_input_1")
        input = """3
2 0
3 1
1 3
4 2
0 4
5 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3
0 0
1 1
5 2
2 3
3 4
4 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """2
2 2
3 3
0 0
1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_5(self):
        logging.info("test_input_5")
        input = """5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()