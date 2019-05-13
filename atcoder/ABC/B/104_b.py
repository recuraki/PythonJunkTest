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
        input = """AtCoder"""
        output = """AC"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """ACoder"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """AcycliC"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """AtCoCo"""
        output = """WA"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """Atcoder"""
        output = """WA"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    s = input()

    if s[0] != "A":
        print("WA")

    else:
        ss = s[1:2] + s[3:-2] + s[-1:]
        flag = True
        for i in range(len(ss)):
            if ss[i] < "a" or ss[i] > "z":
                flag = False

        if flag == False:
            print("WA")
        elif (s[2] == "C" and s[-2] != "C") or\
                (s[2] != "C" and s[-2] == "C"):
            print("AC")
        else:
            print("WA")

