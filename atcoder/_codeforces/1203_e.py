
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int,input().split()))
    orig1 = [0] * 150010
    orig2 = [0] * 150020
    for i in range(n):
        orig1[dat[i]] += 1
    print(orig1[0:10])
    for i in range(1, 150000):
        if i != 1 and orig2[i-1] == 0 and orig1[i] != 0:
            orig1[i] -= 1
            orig2[i-1] += 1
        if orig2[i] == 0 and orig1[i] != 0:
            orig1[i] -= 1
            orig2[i] += 1
        if orig2[i + 1] == 0 and orig1[i] != 0:
            orig1[i] -= 1
            orig2[i+1] += 1
    print(orig1[0:10])
    print(orig2[0:10])
    res = 0
    for i in range(1, 150010):
        if orig2[i] != 0:
            res +=1
    print(res)




class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """6
2 2 2 4 6 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6
1 1 1 4 4 4"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()