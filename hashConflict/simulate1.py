# hash  シミュレータ
PERTURB_SHIFT = 5

used = set()
vala = 10
valb = (10<<10)*5-1
nn = 5
data = []
datb = []


hashval = vala
mask = 2**16 - 1
i = hashval & mask
perturb = hashval

print("-------------------")
res = []

final = []
candi = []
candi.append( 1 )
candi.append( 6 )
candi.append( 31 )
candi.append( 156 )
candi.append( 781 )
candi.append( 3906 )
candi.append( 19531 )
candi.append( 32120 )
candi.append( 29529 )
candi.append( 16574 )
candi.append( 17335 )
candi.append( 21140 )
candi.append( 40165 )
candi.append( 4218 )
candi.append( 21091 )
candi.append( 39920 )
candi.append( 2993 )
candi.append( 14966 )
candi.append( 9295 )
candi.append( 46476 )
candi.append( 35773 )
candi.append( 47794 )
candi.append( 42363 )
candi.append( 15208 )
candi.append( 10505 )
candi.append( 52526 )
candi.append( 487 )
candi.append( 2436 )
candi.append( 12181 )
candi.append( 60906 )


candi = []
candi.append( 20 )
#for i in range(15, 53):
#    candi.append( (20  << i) +20 )
for i in range(10):
    candi.append( (i  << 47) | 20 )
    candi.append( (i  << 47) | 14 )


visited = set()
finalres = -1
for initval in candi:
    print(">> ", initval)
    for loop in range(1,2):
        import collections
        tmp = collections.defaultdict(int)
        tmpmax = -1

        hashval = initval ^ (loop << 0)
        hashval -= loop * 1
        if hashval in visited:
            print("!!!!!!!!!!!!!!!!!!!!!!")
        visited.add(hashval)


        if hashval <= 0:
            continue
        hashval = hash(hashval)
        i = hashval & mask # これについて計算を開始
        perturb = hashval
        ngcnt = 0
        while i in used:
            print(" ng", hashval, loop, "NG ix=", i, "ngcnt", ngcnt, )
            ngcnt +=1
            perturb >>= PERTURB_SHIFT
            i = (i * 5 + perturb + 1) & mask
        print(hashval,loop,  "ok ix=", i, "ngcnt", ngcnt, )
        tmp[ngcnt] += 1
        tmpmax = max(tmpmax, ngcnt)
        finalres = max(finalres, ngcnt)
        used.add(i)
print(finalres)
