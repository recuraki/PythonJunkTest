import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    os = input()
    import  collections
    c = collections.Counter(os)
    res = 99999
    for k in c:
        s = os
        cnt = 0
        while True:
            # 一文字になったなら
            if len(collections.Counter(s)) == 1:
                break
            ss = ""
            for i in range(len(s) - 1):
                if s[i] == k or s[i+1] == k:
                    ss += k
                else:
                    ss += s[i]
            cnt += 1
            s = ss
        res = min(res, cnt)
    print(res)


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
        input = """serval"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """jackal"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """zzz"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """whbrjpjyhsrywlqjxdbrbaomnw"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()