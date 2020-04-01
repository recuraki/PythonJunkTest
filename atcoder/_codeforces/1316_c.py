import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n, m, p = map(int, input().split())
    data = list(map(lambda x: int(x) % p , input().split()))
    datb = list(map(lambda x: int(x) % p , input().split()))
    #print(data)
    #print(datb)
    for i in range (n):
        if data[i] != 0:
            inda = i
            break
    for i in range (m):
        if datb[i] != 0:
            indb = i
            break
    #print(inda, indb)
    print(indb + inda)




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
        input = """3 2 2
1 1 2
2 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2 999999937
2 1
3 1"""
        output = """2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()