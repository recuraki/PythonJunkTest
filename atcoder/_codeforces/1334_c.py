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
        n = int(input())
        data = []
        datb = []
        for i in range(n):
            a, b = map(int, input().split())
            data.append(a)
            datb.append(b)
        for i in range(n):
            k = i + 1 if i != (n - 1) else 0
            datb[i] = min(datb[i], data[k])
        sys.stdout.writelines(str(sum(data) - sum(datb) + min(datb)) + "\n")


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
3
7 15
2 14
5 3
4
1 0
1 100
1 50
2 3
3
1 0
2 1
3 0"""
        output = """6
1
5"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()