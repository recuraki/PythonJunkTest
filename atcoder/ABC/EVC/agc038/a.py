import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    k = int(input())
    x = 0
    cur = ""
    count = 1

    #print("s={0}".format(s))
    for i in range(len(s)):
        #print("i={0}, cur = ".format(i, cur))
        if cur == s[i]:
            count += 1
            #print(" same count = {0}".format(count))
        else:
            x += count // 2
            #print(" change add = {0}".format(count // 2))
            count = 1
        cur = s[i]
    x += count // 2
    #print(" change add = {0}".format(count // 2))
    res1 = x
    #print(res1)

    s = s * 2
    cur = ""
    count = 1
    x=0
    #print("s={0}".format(s))
    for i in range(len(s)):
        #print("i={0}, cur = ".format(i, cur))
        if cur == s[i]:
            count += 1
            #print(" same count = {0}".format(count))
        else:
            x += count // 2
            #print(" change add = {0}".format(count // 2))
            count = 1
        cur = s[i]
    x += count // 2
    #print(" change add = {0}".format(count // 2))
    res2 = x
    #print(res2)

    res = 0

    if k % 2 == 1:
        res += res2 * (k//2)
        res += res1
    else:
        res += res2 * (k//2)

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
        input = """issii
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """sas
2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_111(self):
        print("test_input_111")
        input = """sas
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_1111(self):
        print("test_input_1111")
        input = """s
2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_11111(self):
        print("test_input_11111")
        input = """s
3"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_111111(self):
        print("test_input_111111")
        input = """s
5"""
        output = """2"""
        self.assertIO(input, output)


    def test_input_2(self):
        print("test_input_2")
        input = """qq
81"""
        output = """81"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """cooooooooonteeeeeeeeeest
999993333"""
        output = """8999939997"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()