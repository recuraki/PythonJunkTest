
import itertools
def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]

def do(s):
    s = s.replace(" ", "")
    ol = len(s)
    s = list(s)
    s = list(map(int, s))

    print(s)
    c = 0
    f = False
    while len(s) != 1 and f is False:
        dat = []
        for i in range(len(s) - 1):
            v = abs(s[i] - s[ i +1])
            dat.append(v)
        s = dat
        ss = "".join(list(map(str, dat)))
        ll = countstrs(ss)
        # print(ol-c-1, ll)
        oddcount0 = 0
        evencount0 = 0
        oddcount1 = 0
        evencount1 = 0
        for i in range(len(ll)):
            if ll[i][0] == "1" and ll[i][1 ] %2 == 1:
                oddcount1 += 1
            if ll[i][0] == "0" and ll[i][1 ] %2 == 1:
                oddcount0 += 1
            if ll[i][0] == "1" and ll[i][1 ] %2 == 0:
                evencount1 += 1
            if ll[i][0] == "0" and ll[i][1 ] %2 == 0:
                evencount0 += 1

        # print("0odd:", oddcount0, "0even:", evencount0, "total", oddcount0+evencount0)
        # print("1odd:", oddcount1, "1even:", evencount1, "total", oddcount1+evencount1)
        """
        if (ol-c-1) %2 == 0: #偶数
            if oddcount1 %2 == 1:
                print("? 1")
            else:
                print("? 0")
        else: # 残り奇数
            if oddcount1 %2 == 1:
                print("? 0")
            else:
                print("? 1")
        """

        print((" " *c) + " ".join(list(map(str, dat))))
        c += 1

def do2(s):
    s = s.replace(" ", "")
    ol = len(s)
    s = list(s)
    s = list(map(int, s))
    print(s)
    c = 0
    dat = countstrs(s)
    while len(dat) != 1:
        print(dat)
        res = []
        for i in range(len(dat)):
            # if i !=0:
            #    res.append((1,1))
            if dat[i][0] == 0 and  dat[i][1] != 1:
                res.append( [0, dat[i][1] - 1] )
            elif dat[i][0] == 1 and  dat[i][1] != 1:
                res.append( [0, dat[i][1] - 1] )
            if i != len(dat) - 1 and len(res) > 0 and res[-1][0] == 1:
                res[-1][1] += 1
            elif i != len(dat) - 1:
                res.append([1 ,1])
        dat = res
    print(dat)


do("123123")
do("321321")
do("111000")
do("010101")
do("10101 00000 11111")

do("00000 10101 11111")

do("01110 10101 11111")
do2("01110 10101 11111")

# do("1010111")
# do("10100111")
# do("2313213213123123112112311231233213211123311123123311213")

# 端っこは連続したのを1にしていい
# 残りが偶数個の時、は1奇数が奇数個なら１
# 残りが奇数個の時、は1奇数が偶数個なら１

