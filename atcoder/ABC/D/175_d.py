import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    datp = list(map(lambda x: int(x) - 1, input().split()))
    datc = list(map(int, input().split()))

    # movetalbeは next, scoreの遷移
    movetable = []
    for i in range(35):
        movetable.append([None] * n)

    for i in range(n):
        ne = datp[i]
        score = datc[ne]
        movetable[0][i] = [ne, score]

    for loop in range(1, 35):
        for i in range(n):
            next1, score1 = movetable[loop - 1][i]
            next2, score2 = movetable[loop - 1][next1]
            movetable[loop][i] = [next2, score1 + score2]

    # print(movetable)
    kres = []
    finalres = -99999999999999

    for kk in range(1, min(n + 1, k)):
        # print("k", kk)
        for i in range(n):
            # i start
            cur = i
            score = 0
            for i in range(35):
                if ((kk >> i) & 1) == 1:
                    cur, addscore = movetable[i][cur]
                    score += addscore
            finalres = max(finalres, score)

    kk = k
    # print("k", kk)
    for i in range(n):
        # i start
        cur = i
        score = 0
        for i in range(35):
            if ((kk >> i) & 1) == 1:
                cur, addscore = movetable[i][cur]
                score += addscore
        finalres = max(finalres, score)

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
        input = """5 2
2 4 5 1 3
3 4 -10 -8 8"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3
2 1
10 -7"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 3
3 1 2
-1000 -2000 -3000"""
        output = """-1000"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719"""
        output = """29507023469"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()