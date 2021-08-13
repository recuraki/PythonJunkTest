import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        num0, num1, k = map(int, input().split())
        num = num0 + num1
        base = ("1" * num1) + ("0" * num0)
        x = base
        y = list(base)
        y[num1 - 1] = "0"
        if num0 == 0:
            if k == 0:
                print("Yes")
                print("1"*num1)
                print("1"*num1)
                return
            else:
                print("No")
                return
        if num1 == 1:
            if k == 0:
                print("Yes")
                print("1"*num1 + "0"*num0)
                print("1"*num1 + "0"*num0)
                return
            else:
                print("No")
                return

        if k < num1:
            y = ("1" * (num1 - k) ) + ("0") + ("1" * k) + ("0" * (num0 - 1))
            print("Yes")
            print(x)
            print("".join(y))
            return
        if k > (num0):
            print("No")
            return
        y = list(base)
        y[num1 - 1] = "0"
        y[num1 - 1 + k ] = "1"
        print("Yes")
        print(x)
        print("".join(y))
        y = "".join(y)
        z = int(x, 2) - int(y, 2)
        s = ("{:0" + str(len(x)) + "b}\n").format(z)
        #print("---")
        #print(x)
        #print(y)
        #print(s)
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
        input = """4 2 3"""
        output = """Yes
101000
100001"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2 1"""
        output = """Yes
10100
10010"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4 6"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_3")
        input = """4 9 8"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_41(self):
        print("test_input_3")
        input = """0 10 0"""
        output = """Yes
1111111111
1111111111"""
        self.assertIO(input, output)
    def test_input_42(self):
        print("test_input_3")
        input = """0 10 1"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_41(self):
        print("test_input_3")
        input = """1 9 8"""
        output = """Yes
1111111110
1011111111"""
        self.assertIO(input, output)

    def test_input_42(self):
        print("test_input_3")
        input = """1 9 7"""
        output = """Yes
1111111110
1101111111"""
        self.assertIO(input, output)
    def test_input_41(self):
        print("test_input_3")
        input = """10 1 0"""
        output = """Yes
1111111110
1101111111"""
        self.assertIO(input, output)
    def test_input_42(self):
        print("test_input_3")
        input = """10 1 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()