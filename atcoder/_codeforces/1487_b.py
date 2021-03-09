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
        n, k = map(int, input().split())
        if n % 2 == 0: # even then NO Conflict
            print(((k - 1) % n) + 1)
            return
        # odd
        cycle = n // 2 # 5->2, 7->3 12x34x
        ok = k # Original
        loop = (k - 1) // cycle

        k = ((cycle + 1) * loop) + ((ok-1) % cycle) + 1
        print(((k - 1) % n) + 1)

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
        input = """7
2 1
2 2
3 1
3 2
3 3
5 5
69 1337"""
        output = """1
2
1
3
2
2
65"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
4 1
4 2
4 3
4 4
4 5
4 6
4 7"""
        output = """1
2
3
4
1
2
3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """12
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
5 9
5 10
5 11
5 12"""
        output = """1
2
4
5
2
3
5
1
3
4
1
2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()