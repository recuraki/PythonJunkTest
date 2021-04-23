import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))

    cur = data[0] * datb[0]
    res = cur
    ma = data[0]
    print(cur)
    for i in range(1,n):
        ma = max(ma, data[i])
        cana = ma * datb[i]
        cur = max(cur, ma * datb[i], cana)
        print(cur)


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
3 2 20
1 4 1"""
        output = """3
12
20"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
715806713 926832846 890153850 433619693 890169631 501757984 778692206 816865414 50442173 522507343 546693304 851035714 299040991 474850872 133255173 905287070 763360978 327459319 193289538 140803416
974365976 488724815 821047998 371238977 256373343 218153590 546189624 322430037 131351929 768434809 253508808 935670831 251537597 834352123 337485668 272645651 61421502 439773410 621070911 578006919"""
        output = """697457706539596888
697457706539596888
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
760974252688942308
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026
867210459214915026"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()