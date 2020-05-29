import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        dat1.sort()
        dat2.sort(reverse=True)
        #print(dat1)
        #print(dat2)
        for i in range(k):
            if dat2[i] > dat1[i]:
                dat1[i] = dat2[i]
        print(sum(dat1))


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
2 1
1 2
3 4
5 5
5 5 6 6 5
1 2 5 4 3
5 3
1 2 3 4 5
10 9 10 10 9
4 0
2 2 4 3
2 4 2 3
4 4
1 2 2 1
4 4 5 4"""
        output = """6
27
39
11
17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()