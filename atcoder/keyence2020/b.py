import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())

    dat = []
    for _ in range(n):
        x, l = map(int, input().split())
        #           0  1   2    3    4co     5
        dat.append([x, l, x - l, x + l, 0, []])
    dat.sort(key=lambda x: x[1], reverse=True)
    # print(dat)
    res = []
    res_safe = []

    def do_count():
        for i in range(n):
            # print("i={0}".format(i))
            c = 0
            m = []
            for j in range(i + 1, n):
                # print("j={0}".format(j))
                if dat[j][3] <= dat[i][2] or dat[i][3] <= dat[j][2]:
                    pass
                else:
                    dat[i][5].append(dat[j])
                    dat[j][5].append(dat[i])
                    dat[i][4] += 1
                    dat[j][4] += 1

    do_count()
    dat.sort(key=lambda x: (x[4], x[1]), reverse=True)
    # print(dat)
    for i in range(n):
        if dat[i][4] == 0:
            res.append(dat[i])
            continue
        # print("node {0}: kill".format(i))
        for node in dat[i][5]:
            # print(node[5])
            for x in range(len(node[5])):
                if node[5][x] == dat[i]:
                    node[4] -= 1
                    del node[5][x]
                    # print("!!!!")

    # print(res)
    print(len(res))


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
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()