

l = [4,3,1,0,0,-1,6,4]
zatsu = sorted(set(l))
zatsuTable = dict()
zatsuTableRev = dict()
for ind, value in enumerate(zatsu):
    zatsuTable[value] = ind
    zatsuTableRev[ind] = value
newl = []
for x in l:
    newl.append(zatsuTable[x])
print(l)
print(newl)