
l = [1,2,3,4,5]
lenTreeList = 2 ** (len(l) - 1).bit_length()
depthTreeList = (len(l) - 1).bit_length()
print("deTL{0}".format(depthTreeList))
for i in range(2**depthTreeList):
    dan = ((i + 1).bit_length() - 1)
    nagasa = 2 ** dan
    banme = (i + 1) - nagasa
    tannilen = (2 ** (depthTreeList) ) // 2 ** dan
    perLen =  (banme * tannilen)
    perLenEnd = perLen + tannilen
    print("i={6}  danme = {0}, nodes_in_this_dan = {1}, banme={2} tannilen={3} perlenl,r={4},{5}".format(dan, nagasa, banme,tannilen, perLen,perLenEnd, i))
