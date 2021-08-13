import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
        h, w, n = map(int, input().split())
        dath = []
        datw = []
        for _ in range(n):
            a, b = map(int, input().split())
            dath.append(a)
            datw.append(b)

        zatsu = sorted(set(dath))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newh = []
        for x in dath:
            newh.append(zatsuTable[x] + 1)

        zatsu = sorted(set(datw))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        neww = []
        for x in datw:
            neww.append(zatsuTable[x] + 1)

        for i in range(n):
            print(newh[i], neww[i])

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
        input = """4 5 2
3 2
2 5"""
        output = """2 1
1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000000 1000000000 10
1 1
10 10
100 100
1000 1000
10000 10000
100000 100000
1000000 1000000
10000000 10000000
100000000 100000000
1000000000 1000000000"""
        output = """1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()