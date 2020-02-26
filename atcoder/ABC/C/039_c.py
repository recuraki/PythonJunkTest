import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def rotateStr(s, i):
        l = len(s)
        return s[i:] + s[:i]
    ss = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
    ssdat = []
    ssdat.append("Do")
    ssdat.append("Do")
    ssdat.append("Re")
    ssdat.append("Re")
    ssdat.append("Mi")
    ssdat.append("Fa")
    ssdat.append("Fa")
    ssdat.append("So")
    ssdat.append("So")
    ssdat.append("La")
    ssdat.append("La")
    ssdat.append("Si")
    s = input()
    for i in range(len(s)):
        #print(s)
        #print(rotateStr(ss, i)[:20])
        if s == rotateStr(ss, i)[:20]:
            break
    print(ssdat[i])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """WBWBWWBWBWBWWBWBWWBW"""
        output = """Do"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """WWBWBWBWWBWBWWBWBWBW"""
        output = """Mi"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()