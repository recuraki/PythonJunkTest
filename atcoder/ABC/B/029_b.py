import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    res = 0
    for i in range(12):
        if input().find("r") != -1:
            res += 1
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
    def test_input1(self):
        print("test_input1")
        input = """january
february
march
april
may
june
july
august
september
october
november
december"""
        output = """8"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """rrrrrrrrrr
srrrrrrrrr
rsr
ssr
rrs
srsrrrrrr
rssrrrrrr
sss
rrr
srr
rsrrrrrrrr
ssrrrrrrrr"""
        output = """11"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()