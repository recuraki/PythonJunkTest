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
        a,b = map(int, input().split())
        if a == 1:
            print(0)
            return
        res = 0
        i = 1
        while True:
            init = i * (i + 2)
            rest = a - init
            if rest < 0:
                break
            cnt = (rest // i) + 1
            res += max(0,min(cnt, b - i))
            i += 1
        print(res)


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
        input = """9
3 4
2 100
4 3
50 3
12 4
69 420
12345 6789
123456 789
12345678 9"""
        output = """1
0
2
3
5
141
53384
160909
36"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()