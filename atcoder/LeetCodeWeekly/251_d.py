from typing import List, Tuple
from pprint import pprint

from collections import defaultdict

revtable = dict()
namehash = dict()
hash2filename = dict()
hash2fullname = dict()

def list2hash(l):
    path = "/" + "/".join(l)
    dir = "/".join(path.split("/")[:-1])
    basename = "/".join(path.split("/"))
    filename = l[-1]
    #print(path, dir,basename)
    dirhash = hash(dir)
    basehash = hash(basename)
    revtable[dirhash] = dir
    revtable[basehash] = basename
    hash2filename[basehash] = filename
    hash2fullname[basehash] = basename
    #print(dir, basename, basehash, filename)
    return dirhash, basehash

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        hash2fullname[0] = "/"
        hash2filename[0] = ""
        totalhash = dict()
        totalhashCount = defaultdict(int)
        curnode2total = dict()
        totalhashCount[0] = 1

        def f(curnode):
            total = 0
            for nextnode in g[curnode]:
                total += f(nextnode)
            #print("out", hash2fullname[curnode], curnode, "Total", total)
            totalhash[curnode] = total

            totalhashCount[total] += 1
            total += hash(hash2filename[curnode])
            curnode2total[curnode] = total



            return total

        res = []
        def gg(curnode):
            total = totalhash[curnode]
            name = hash2fullname[curnode]
            #print(name, totalhashCount[total])
            if totalhashCount[total] > 1 and total != 0: return
            #print(name, total, totalhashCount[total])
            if name != "/" or total==0:
                res.append(name.split("/")[1:])
            for nextnode in g[curnode]:
                gg(nextnode)

        g = defaultdict(lambda : set())
        for p in paths:
            dirhash, basehash = list2hash(p)
            g[dirhash].add(basehash)
        f(0)
        gg(0)
        return(res)




st = Solution()

print(st.deleteDuplicateFolder(paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))
print(st.deleteDuplicateFolder(paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]))
print(st.deleteDuplicateFolder(paths = [["a","b"],["c","d"],["c"],["a"]]))
print(st.deleteDuplicateFolder(paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]))
print(st.deleteDuplicateFolder(paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]))

