
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = list()
        for l in image:
            t = []
            for i in range(len(l)-1, -1, -1):
                t.append(1 if l[i] == 0 else 0)
            ans.append(t)
        return ans
