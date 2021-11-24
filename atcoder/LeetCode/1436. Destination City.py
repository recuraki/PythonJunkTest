class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        c = set()
        for a, b in paths:
            d[a] = b
            c.add(a)
            c.add(b)
        for x in c:
            if x not in d: return x

