import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    def do():
        s = input()
        if s.count("0") == 0:
            print("YES")
            return
        if s.count("1") == 0:
            print("YES")
            return
        can = True
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i+1]):
                can = False
                break
        if can:
            print("YES")
            return


        l = len(s)
        erase = []
        for kiri in range(l + 1):
            erase = []
            for i in range(0, kiri):
                if s[i] == "1":
                    erase.append(i)
            for i in range(kiri,l):
                if s[i] == "0":
                    erase.append(i)
            cur = -100
            can = True
            #print(kiri, erase)
            for x in erase:
                if x - cur < 2:
                    can = False
                    break
                cur = x
            if can:
                print("YES")
                return
        print("NO")



    q = int(input())
    for _ in range(q):
        do()
    # do()


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
        input = """1
0000010"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """7
10101011011
0000
11111
110
1100
0000010
1111110"""
        output = """YES
YES
YES
YES
NO
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()