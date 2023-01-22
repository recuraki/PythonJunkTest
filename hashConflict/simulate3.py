
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
candi.append( 0 )
candi.append( 0 )
candi.append( 0 )
candi.append( 0 )
candi.append( 0 )

visited = set()
finalres = -1
for initval in candi:
    print(">> ", initval)
    for loop in range(1,2):
        import collections
        tmp = collections.defaultdict(int)
        tmpmax = -1

        hashval = initval
        if hashval in visited:
            print("!!!!!!!!!!!!!!!!!!!!!!")
        visited.add(hashval)


        #if hashval <= 0:
        #    continue
        hashval = hash(hashval)
        i = hashval & mask # これについて計算を開始
        perturb = hashval
        ngcnt = 0
        while i in used:
            print(" ng", hashval, loop, "NG ix=", i, "ngcnt", ngcnt, )
            ngcnt +=1
            perturb >>= PERTURB_SHIFT
            print("  > calc", i * 5, perturb, 1, "mask=", (i * 5 + perturb + 1) & mask)
            i = (i * 5 + perturb + 1) & mask
        print("OK", initval ,hashval,loop,  "ok ix=", i, "ngcnt", ngcnt, )
        tmp[ngcnt] += 1
        tmpmax = max(tmpmax, ngcnt)
        finalres = max(finalres, ngcnt)
        used.add(i)
print(finalres)
