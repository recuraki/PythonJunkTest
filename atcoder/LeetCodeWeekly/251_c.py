from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        from itertools import permutations
        questionnum = len(students[0]) # 質問の数
        personnum = len(students) # 人数
        perm = list(range(personnum))
        score = [[-1] * personnum for _ in range(personnum)]
        for i in range(personnum):
            for j in range(personnum):
                curscore = 0
                for k in range(questionnum):
                    if students[i][k] == mentors[j][k]: curscore += 1
                score[i][j] = curscore
        #print(score)
        res = -1
        for newp in permutations(perm, personnum):
            curscore = 0
            for k in range(personnum):
                #print(newp[k])
                #print(score[k])
                curscore += score[k][newp[k]]
            #print(newp, curscore)
            res = max(res, curscore)
        return res




st = Solution()

print(st.maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]))
print(st.maxCompatibilitySum(students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]))
print(st.maxCompatibilitySum([[0,1,0,1,1,1],[1,0,0,1,0,1],[1,0,1,1,0,0]], [[1,0,0,0,0,1],[0,1,0,0,1,1],[0,1,0,0,1,1]]))

