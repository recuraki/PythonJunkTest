import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    q = int(input())
    for _ in range(q):
        n, m =map(int, input().split())
        data = list(map(int, input().split())) # to n
        datp = list(map(int, input().split())) # to m
        canchange = [False] * 2000
        for i in range(len(datp)):
            canchange[datp[i] - 1] = True
        #print(canchange)

        f = True
        while True:
            nochange = True
            for i in range(n - 1):
                if data[i] > data[i + 1]:
                    if canchange[i]:
                        data[i], data[i+1] = data[i+1], data[i]
                        nochange=False
                    else:
                        nochange=True
                        f = False
                        break
            if nochange:
                break
        print("YES" if f else "NO")


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
        input = """6
5 4
5 4 3 2 1
1 2 3 4
4 2
4 1 2 3
3 2
5 1
1 2 3 4 5
1
4 2
2 1 4 3
1 3
4 2
4 3 2 1
1 3
5 2
2 1 2 3 3
1 4"""
        output = """YES
NO
YES
YES
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()