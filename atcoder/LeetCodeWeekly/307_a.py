from typing import List, Tuple
from pprint import pprint


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        Ene = initialEnergy
        Exp = initialExperience
        needEne = 0
        needExp = 0
        n = len(energy)
        for i in range(n):
            tekiEne = energy[i]
            tekiExp = experience[i]
            needExp = max((tekiExp+1) - Exp, needExp)
            needEne = max((tekiEne+1) - Ene, needEne)
            Ene -= tekiEne
            Exp += tekiExp
        return needEne+ needExp



st = Solution()

print(st.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])==8)
print(st.minNumberOfHours( initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3])==0)

