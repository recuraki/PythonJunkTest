import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    l = len(s)
    res = 0
    for i in range(l):
        #print("i:", i)
        if s[i] == "U":
            #print("U")

            # 自分より下の階のケア
            a = 2 * i
            res += a
            #print(a)

            # 自分より上の階のケア
            a = l - (i + 1)
            res += a
            #print(a)
        else:
            #print("D")
            # 自分より下の階のケア
            a = i
            res += a
            #print(a)

            # 自分より上の階のケア
            a = 2 * (l - (i + 1))
            res += a
            #print(a)

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
        print("test_input_1")
        input = """UUD"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """UUDUUDUD"""
        output = """77"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()