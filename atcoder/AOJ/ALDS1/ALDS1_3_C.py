import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import collections
    d = collections.deque([])
    for _ in range(n):
        s = input().split()
        if s[0] == "deleteFirst":
            d.popleft()
        elif s[0] == "deleteLast":
            d.pop()
        elif s[0] == "insert":
            d.appendleft(s[1])
        else:
            try:
                d.remove(s[1])
            except:
                pass
    print(" ".join(d))




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
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5"""
        output = """6 1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
deleteFirst
deleteLast"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()