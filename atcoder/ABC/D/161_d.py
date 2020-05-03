import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k = int(input())
    if k < 11:
        print(k)
    else:
        s = [None] * 20
        target = k
        target -= 10
        s[1] = 1
        for i in range(target):
            # print(s[::-1])
            for j in range(20):
                if s[j] is None:
                    s[j] = 0
                # print("add try j=",j, "s[j]",s[j], "->", s[j] + 1)
                s[j] += 1  # その桁を足す

                if s[j] > 9:  # もし10になったら
                    # print("reach 10")
                    s[j] = 0
                    continue  # 続ける

                if j != 0:
                    # print(" j!=1")
                    for k in range(j, -1, -1):
                        if s[k] == 0:
                            s[k - 1] = 0
                        else:
                            s[k - 1] = s[k] - 1

                if s[j + 1] != None and abs(s[j] - s[j + 1]) > 1:
                    # print(" over")
                    continue
                # print(" pass")
                break
        #print(s)
        res = ""
        for i in range(20):
            if s[i] != None:
                res = str(s[i]) + res
            else:
                break
        print(int(res))


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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """13"""
        output = """21"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()