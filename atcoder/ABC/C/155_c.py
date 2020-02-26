import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import collections
    dat = []
    for _ in range(n):
        dat.append(input())
    c = collections.Counter(dat)
    mcc = c.most_common(1)[0][1]
    #print(mcc)
    res = []
    for k in c:
        if c[k] == mcc:
            res.append(k)
    res.sort()
    for i in range(len(res)):
        print(res[i])


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
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()