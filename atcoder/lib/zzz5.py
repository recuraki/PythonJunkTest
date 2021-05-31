dat = [0,2,3,4,100,101,7,10,8,0]
lele = len(dat)
res = 0
for l in range(lele):
    for r in range(l+1, lele):
        buf = dat[l:r+1]
        cnt  = 0
        for i in range(len(buf)):
            for j in range(i+1, len(buf)):
                if buf[i] == buf[j]:
                    cnt += 1
        res += cnt
        print(buf, cnt)
print(dat, res)
