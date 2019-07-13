import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int,input().split()))

    dat = [0] + dat + [0]
    total = 0
    cur = 0
    for i in range(n + 2):
        total += abs(cur - dat[i])
        cur = dat[i]
    total += abs(cur)
    cur = 0
    for i in range(n):
        j = i + 1
        if dat[j-1] < dat[j] < dat[j+1]:
            # 間に挟まれているパターン１
            #print("pat1")
            print(total)
        elif dat[j-1] > dat[j] > dat[j+1]:
            # 間に挟まれているパターン2
            #print("pat2")
            print(total)
        else:
            # この場合は間に挟まれていない
            #print("{0} {1} {2}".format(total, abs(dat[j-1] -dat[j]) , abs(dat[j-1] -dat[j+1])))
            print(total - abs(dat[j-1] -dat[j]) - abs(dat[j] -dat[j+1]) + abs(dat[j-1] - dat[j+1]))

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
        input = """3
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()