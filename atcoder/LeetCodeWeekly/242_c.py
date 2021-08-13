
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #if s[-1] == "1":
        #    return False
        l = len(s)
        eventin = [0] * (l*3)
        eventout = [0] * (l*3)
        eventin[0] += 1
        eventout[0] += 1
        canReach = [False] * l
        cnt = 0
        for i in range(l):
            can = True
            if s[i] == "1": # 壁ならだめ
                can = False
            cnt += eventin[i]
            if cnt <= 0:
                can = False
            if can:
                #print("can ",i, canReach)
                canReach[i] = True
                eventin[min(i+minJump, 10**18)] += 1
                eventout[min(i+maxJump, 10**18)] += 1
                #print(eventin)
                #print(eventout)
                #print("can ", i, canReach)
            cnt -= eventout[i]
        #print(canReach)
        return canReach[l-1]





st = Solution()

print(st.canReach(s = "011010", minJump = 2, maxJump = 3) == True)
print(st.canReach(s = "01101110", minJump = 2, maxJump = 3) == False)
print(st.canReach("01", 1, 1) == False)
print(st.canReach("00111010", 3, 5) == False)