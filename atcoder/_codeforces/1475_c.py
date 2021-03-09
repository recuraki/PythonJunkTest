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
        a, b, k = map(int, input().split())
        data = list(map(lambda x: int(x) - 1, input().split()))
        datb = list(map(lambda x: int(x) - 1, input().split()))
        ea = [[] for _ in range(a)]
        eb = [[] for _ in range(b)]
        for i in range(k):
            ea[data[i]].append(datb[i])
            eb[datb[i]].append(data[i])
        res = 0
        for i in range(k):
            x, y = data[i], datb[i]
            res += k - (len(ea[x]) + len(eb[y]) - 1)
        print(res//2)

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
        input = """3
3 4 4
1 1 2 3
2 3 2 4
1 1 1
1
1
2 2 4
1 1 2 2
1 2 1 2"""
        output = """4
0
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()