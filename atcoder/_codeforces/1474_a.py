import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        s = input()
        prev = "0"
        res = []
        res2 = []
        for i in range(n):
            if s[i] == "0":
                if prev == "0":
                    res.append("1")
                    res2.append("1")
                    prev = "1"
                    continue
                if prev == "1":
                    res.append("0")
                    res2.append("0")
                    prev = "0"
                    continue
                if prev == "2":
                    res.append("1")
                    res2.append("1")
                    prev = "1"
                    continue
            if s[i] == "1":
                if prev == "0":
                    res.append("2")
                    res2.append("1")
                    prev = "2"
                    continue
                if prev == "1":
                    res.append("2")
                    res2.append("1")
                    prev = "2"
                    continue
                if prev == "2":
                    res.append("1")
                    res2.append("0")
                    prev = "1"

                    continue
        print("".join(res2))


    q = int(input())
    for _ in range(q):
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
        input = """5
1
0
3
011
3
110
6
111000
6
001011"""
        output = """1
110
100
101101
101110"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
1
1
"""
        output = """1
"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()