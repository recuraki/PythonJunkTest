import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    n = int(input())
    d = {}

    for waza_number in range(1, n + 1):
        waza_info = input().split(" ")
        d[waza_number] = (int(waza_info[0]), set([int(w) for w in waza_info[2:]]))

    required = set([n])
    unseen = d[n][1]

    while len(unseen) > 0:
        waza_number = unseen.pop()
        required.add(waza_number)
        unseen = unseen | (d[waza_number][1] - required)

    cost = 0
    for waza_number in required:
        cost += d[waza_number][0]

    print(cost)


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
3 0
5 1 1
7 1 1"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4"""
        output = """5000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()