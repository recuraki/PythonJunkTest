import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import heapq
    d = []
    while True:
        s = input().split()
        if s[0] == "end":
            break
        if s[0] == "insert":
            heapq.heappush(d, -int(s[1]))
        if s[0] == "extract":
            c = heapq.heappop(d)
            print(-c)





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
        input = """insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end"""
        output = """8
10
11
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()