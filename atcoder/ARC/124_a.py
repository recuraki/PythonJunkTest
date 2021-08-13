import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        mod = 998244353
        n, k = map(int, input().split())
        canuse = set(list(range(1, k+1)))
        fixed = [False] * n
        addEvent = [None] * n
        delEvent = [None] * n

        for i in range(k):
            num = i + 1
            a, b = input().split()
            b = int(b)
            b -= 1
            if a == "L":
                canuse.remove(num)
                addEvent[b] = num
                fixed[b] = True
            else: #"R"
                delEvent[b] = num
                fixed[b] = True

        res = 1

        for i in range(n):
            if fixed[i] is False:
                res *= len(canuse)
                res %= mod
            if addEvent[i] is not None: canuse.add(addEvent[i])
            if delEvent[i] is not None: canuse.remove(delEvent[i])
            #print("i", i, canuse, res)

        print(res % mod)


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
        input = """3 2
L 1
R 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """30 10
R 6
R 8
R 7
R 25
L 26
L 13
R 14
L 11
L 23
R 30"""
        output = """343921442"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()