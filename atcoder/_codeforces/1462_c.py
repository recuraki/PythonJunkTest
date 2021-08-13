import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys



    q = int(input())
    def do(ketai, cur, m, target):
        l = len(cur)
        if l > ketai:
            return None

        for i in range(m, 10):
            next = cur + [i]
            if sum(next) == target:
                return next

        for i in range(m, 10):
            next = cur + [i]
            res = do(ketai, next, i + 1, target)
            if res != None:
                return res


    for _ in range(q):
        n = int(input())
        for keta in range(1, 10):
            res = do(keta, [], 1, n)
            if res != None:
                break
        if res == None:
            print(-1)
        else:
            print("".join(list(map(str, res))))


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
        input = """4
1
5
15
50"""
        output = """1
5
69
-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()