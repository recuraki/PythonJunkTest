#! env python

l1 = " switchport trunk allowed vlan "
l2 = " switchport trunk allowed vlan add "

def MergeSeries(liSrc):
    if liSrc == []:
        return []
    if len(liSrc) == 1:
        return liSrc
    getCurBuf = lambda l: l[0] if l[0] == l[-1] else l[0] + "-" + l[-1]
    liRes = list()
    buf = list()
    pNum = int(liSrc.pop(0))
    buf.append(str(pNum))
    while liSrc:
        cNum = int(liSrc.pop(0))
        if (cNum - pNum) != 1:
            liRes.append(getCurBuf(buf))
            buf = [str(cNum)]
        else:
            buf.append(str(cNum))
        pNum = cNum

    if (cNum - pNum) != 1:
        liRes.append(getCurBuf(buf))
        buf = []

    return liRes

def MergeStrToLimit(prefix, liStr, sep = ",", lim=78):
    res = prefix
    buf = list()
    while liStr:
        s = liStr.pop(0)
        if (len(res) + len(s) ) > lim:
            liStr.insert(0, s)
            break
        else:
            buf.append(s)
            res = prefix + sep.join(buf)
    return res, liStr
    

def vlanstr(s):
    liv = s.split(",")
    liv.sort()
    liv = MergeSeries(liv)
    r, liv = MergeStrToLimit(l1, liv)
    while liv:
        out, liv = MergeStrToLimit(l2, liv)
        r = r + "\n" + out
    return(r)

x = "10"
print(vlanstr(x))
x = "2001,2003,2005,2007,2009,3001,3003,3005,3007,3009"
print(vlanstr(x))
x = "1000,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056,1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088,1090,1092,1094,1096,1098,1100,1102,1104,1106,1108,1110,1112,1114,1116,1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,1138,1140,1142,1144,1146,1148,1150,1152,1154,1156,1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,1178,1180,1182,1184,1186,1188,1190,1192,1194,1196,1198"
print(vlanstr(x))

