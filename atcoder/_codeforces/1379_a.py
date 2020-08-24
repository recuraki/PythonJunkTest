import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #input = sys.stdin.readline

    from pprint import pprint
    import sys
    def count_aba(s):
        param = "abacaba"
        res = 0
        for i in range(len(s)):
            if str(s[i:i + len(param)]) == str(param):
                res += 1
        return res

    def do():
        n = int(input())
        os = input()
        didmake = False
        for i in range(n - 6):
            s = os
            #print(i)
            # check
            isfit = True
            for j in range(len(param)):
                if s[i + j] == "?" or s[i + j] == param[j]:
                    continue
                isfit = False
                break
            if isfit is False:
                continue
            if s[i + len(param):].count(param) == 0:
                res = list(os.replace("?", "z"))
                for j in range(len(param)):
                    res[i+j] = param[j]
                res = "".join(res)
                if count_aba(res) != 1:
                    continue
                didmake = True
                print("Yes")
                print("".join(res))
                return
        if didmake is False:
            print("No")
            return

    param = "abacaba"
    q = int(input())
    for _ in range(q):
        do()




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
        input = """6
7
abacabz
7
???????
11
aba?abacaba
11
abacaba?aba
15
asdf???f???qwer
11
abacabacaba"""
        output = """No
Yes
abacaba
Yes
abadabacaba
Yes
abacabadaba
No
No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()