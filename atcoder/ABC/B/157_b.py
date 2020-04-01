import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    dat = []
    isok = []
    for _ in range(3):
        l = list(map(int, input().split()))
        dat.append(l)
        isok.append([False] * 3)
    n = int(input())
    for _ in range(n):
        c = int(input())
        for i in range(3):
            for j in range(3):
                if dat[j][i] == c:
                    isok[i][j] = True
    if isok[0][0] and isok[0][1] and isok[0][2]:
        print("Yes")
    elif isok[1][0] and isok[1][1] and isok[1][2]:
        print("Yes")
    elif isok[2][0] and isok[2][1] and isok[2][2]:
        print("Yes")
    elif isok[0][0] and isok[1][0] and isok[2][0]:
        print("Yes")
    elif isok[0][1] and isok[1][1] and isok[2][1]:
        print("Yes")
    elif isok[0][2] and isok[1][2] and isok[2][2]:
        print("Yes")
    elif isok[0][0] and isok[1][1] and isok[2][2]:
        print("Yes")
    elif isok[2][0] and isok[1][1] and isok[0][2]:
        print("Yes")
    else:
        print("No")


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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()