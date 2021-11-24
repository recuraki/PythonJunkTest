import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    n = int(input())
    keta = len(str(n))
    res = [0] * keta
    for i in range(0, keta):
        res[i] = i * 10 ** (keta - i - 1)
        base = "1" * (i + 1) + "0" * (keta - i - 1)
        ma = int(base.replace("0", "9")) + 1
        cnt = min(n, ma) - int(base)
        res[i] += max(0, cnt)
    for i in range(keta):
        if str(n)[i] != "1": break
        res[i] += 1
    print(sum(res))


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
        input = """11"""
        output = """4"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """120"""
        output = """44"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """987654321"""
        output = """123456789"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()