import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    res = [-1] * n
    f = True
    for i in range(m):
        s, c = map(int, input().split())
        s -= 1 # 0 ind
        if res[s] == -1 or res[s] == c:
            res[s] = c
        else:
            f = False

    if res[0] == -1 and n != 1:
        res[0] = 1

    res = list(map(lambda x: x if x != -1 else 0, res))
    #print(res)

    num = int("".join(list(map(str, res))))
    #print(res)
    #print(num)

    if len(str(num)) != n:
        f = False

    if f is True:
        res = "".join(list(map(str, res)))
        print(res)
    else: # False
        print(-1)



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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2 1
2 1"""
        output = """11"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """1 1
1 0"""
        output = """0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()