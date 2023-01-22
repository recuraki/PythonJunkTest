from typing import List, Tuple
from pprint import pprint


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        from collections import defaultdict
        movies = defaultdict(list)
        cnt = defaultdict(int)
        for i in range(len(creators)):
            cre = creators[i]
            id = ids[i]
            vcnt = views[i]
            cnt[cre] += vcnt
            movies[cre].append( (-vcnt, id) )
        maxview = -1
        maxcre = []
        for k in set(creators):
            maxview = max(maxview, cnt[k])
        for k in set(creators):
            if cnt[k] == maxview:
                maxcre.append(k)
        #print(maxcre)
        ans = []
        for k in maxcre:
            movies[k].sort()
            ans.append([k, movies[k][0][1]])
        #print(ans)
        return ans



st = Solution()

print(st.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4])==[["alice","one"],["bob","two"]])
print(st.mostPopularCreator(creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2])==[["alice","b"]])

