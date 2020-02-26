import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    t = input()
    res = s+t
    kekka = n*2
    import copy
    for i in range(n):
        tmp = list(res)
        del tmp[n]
        target = "".join(tmp)
        if target[:n] == s and target[-n:] == t:
            kekka = len(target)
            #print(target)
        res = copy.deepcopy(tmp)

    print(kekka)

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
abc
cde"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
abcde
dexxx"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
expr
expr"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()