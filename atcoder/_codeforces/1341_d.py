import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    led = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
    led = [int(led[i], 2) for i in range(10)]
    ledbin = [bin(led[i])for i in range(10)]
    ledbinc = [str(bin(led[i])).count("1") for i in range(10)]





    n, k = map(int, input().split())
    dat = []
    for _ in range(n):
        s = input()
        dat.append(int(s, 2))
    #print(dat)
    res = [0] * n
    ind = 0
    resk = k
    bufferK = [-1] * n
    candidate = [9] * n
    is_ok = False
    while True:
        if ind == n:
            if bufferK[ind] == 0:
                is_ok = True
                break
            else:
                return None
        # print(" > call do dat", dat, "ind", resk, "resk", resk, "can", candidate)
        while candidate[ind] >= 0:
            canNum = candidate[ind]
            negatar = 255 ^ led[canNum]
            if negatar & dat[ind] != 0:
                continue
            needline = bin(led[canNum]).count("1") - str(bin(dat[ind] & led[canNum])).count("1")
            if needline <= resk:
                ind += 1


    if is_ok is False:
        print(-1)
    else:
        print("".join(list(map(str, res))))



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
        input = """1 7
0000000"""
        output = """8"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 5
0010010
0010010"""
        output = """97"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 5
0100001
1001001
1010011"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()