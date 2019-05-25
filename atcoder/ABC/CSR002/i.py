def resolve():
    dat = []
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        dat.append((a,b))

    canwin = False

    for i in range(n):
        allwin = True
        for j in range(n):
            if i == j:
                print("!")
                break
            if (dat[j][0] / dat[i][1]) >= (dat[i][0] / dat[j][1]):
                print("{0} cannnot win {1}".format(i,j))
                allwin = False
                break
        if allwin:
            print(i + 1)
            canwin = True
            break
    if canwin is False:
        print("-1")





import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
7 3
9 2
2 5"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
999999999 1000000000
1 999999999"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
999999999 1
1000000000 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3
100 17
171 10
91 19"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()