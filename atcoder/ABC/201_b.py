import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        dat.append([t,s])
    dat.sort(reverse=True)
    print(dat[1][1])
    #print(dat)

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
Everest 8849
K2 8611
Kangchenjunga 8586"""
        output = """K2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
Kita 3193
Aino 3189
Fuji 3776
Okuhotaka 3190"""
        output = """Kita"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390"""
        output = """QCFium"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()