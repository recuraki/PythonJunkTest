import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat_b = list(map(int, input().split()))

    dat = []
    for i in range(n):
        dat.append((dat_a[i], dat_b[i]))
    dat.sort(key=lambda x: (x[1], x[0]))

    dat_a = []
    dat_b = []
    for i in range(n):
        dat_a.append(dat[i][0])
        dat_b.append(dat[i][1])

    can = True
    count = 0
    for i in range(n):
        #print(dat_a)
        #print(dat_b)
        #print("----[{0}]".format(i))

        if dat_a[i] > dat_b[i]:
            sind = -1
            snum = 999999999999
            for j in range(i+1, n):
                #print("check {0} <= {1}".format(dat_a[j], dat_b[i]))
                if dat_a[j] <= dat_b[i]:
                    #print("yes")
                    if sind == -1 and dat_a[j] < snum:
                        sind = j
                        snum = dat_a[j]
            if sind != -1:
                #print("find {0} <-> {1} index {2},{3}".format(dat_a[i], dat_a[sind],i, sind))
                count += 1
                dat_a[i], dat_a[sind] = dat_a[sind], dat_a[i]
            else:
                can = False

    #print(count)
    if can is False:
        print("No")
    elif count > (n-2):
        print("No")
    else:
        print("Yes")





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
        input = """3
1 3 2
1 2 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2 3
2 2 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
3 1 2 6 3 4
2 2 8 3 4 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """7
6 5 4 3 2 1 7
1 2 3 4 5 6 7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_32(self):
        print("test_input_32")
        input = """2
2 1
1 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_33(self):
        print("test_input_33")
        input = """2
1 2
1 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_322(self):
        print("test_input_322")
        input = """5
5 7 7 3 3
3 3 5 7 7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_3222(self):
        print("test_input_3222")
        input = """5
7 3 5 3 7
3 7 3 7 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_32122(self):
        print("test_input_32122")
        input = """6
7 7 3 3 5 5
3 3 5 5 7 7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_32122(self):
        print("test_input_32122")
        input = """6
7 3 5 5 3 7
3 5 7 7 5 3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()