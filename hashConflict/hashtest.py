# hash  シミュレータ

def sim(candi):
    #print("hash sim. you want to add {0} to hashtable".format(candi))
    PERTURB_SHIFT = 5

    used = set() # 今回は簡単に使っているかのテストのみ
    nn = 5
    data = []
    datb = []
    mask = 2**16 - 1 # 簡易化のため、ハッシュサイズはある程度大きいと仮定

    res = []
    final = []

    visited = set()
    finalres = -1
    ma = 0
    for initval in candi:
        hashval = initval

        hashval = hash(hashval)
        i = hashval & mask # これについて計算を開始
        perturb = hashval # forの初期化部分
        ngcnt = 0 # ixを計算しなおした数
        while i in used:
            print("NG ix=", i, "ngcnt", ngcnt, "perturb", perturb)
            ngcnt +=1
            perturb >>= PERTURB_SHIFT
            i = (i * 5 + perturb + 1) & mask
        print("OK", ngcnt, initval ,hashval,  "ok ix=", i, "ngcnt", ngcnt, )
        ma = max(ma,ngcnt)
        used.add(i)
    return ma

sim([0,1,2,3])
ma=0
for k in range(30):
    #ma = sim([i* (2**58 + (2**k) ) for i in range(128)])
    print(k, ma)

sim([i << 50 for i in range(1000)])

#print(bin(1 * 2**64 - 1))
#print(bin(2 * (2**64 - 16)))
#print(bin(2**64 - 1).count("1"))
