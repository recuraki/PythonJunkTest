"""
0から始まるハッシュを列挙する
"""
import sys

PERTURB_SHIFT = 5

used = set()
vala = 10
valb = (10<<10)*5-1
nn = 5
data = []
datb = []


hashval = vala
mask = 2**16 - 1 # これがmask
i = hashval & mask
perturb = hashval

print("-------------------")
res = []

perturb = 0 # hash事前計算
i = perturb
#data.append(i)
for loop in range(30):
    perturb >>= PERTURB_SHIFT
    i = (i * 5 + perturb + 1) & mask
    data.append(i)
print(data)
for x in data:
    print("candi.append(", x, ")")
