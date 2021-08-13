
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    lastplus = 0
    lastminus = 0
    res = []
    for i in range(1,a+1):
        res.append(i)
        lastplus = i - 1
    for i in range(1,b+1):
        res.append(-i)
        lastminus = a + i - 1
    #print(res)
    #print(lastplus, lastminus)
    #print(res[lastplus], res[lastminus])
    ss = sum(res)
    #print("sum", ss)
    if ss < 0:
        res[lastplus] += abs(ss)
    elif ss > 0:
        res[lastminus] -= abs(ss)
    #print(sum(res))
    print(" ".join(list(map(str, res))))


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
        input = """1 1"""
        output = """1001 -1001"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 4"""
        output = """-8 -6 -9 120 -97"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 5"""
        output = """323 -320 411 206 -259 298 -177 -564 167 392 -628 151"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()