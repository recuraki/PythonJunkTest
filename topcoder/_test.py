class Scissors():
    def openingTime(self, N):
        i=1
        total = 10
        while(N>(2**i)):
            i+=1
            total+= 10
        return total


class Scissors():
    def openingTime(self, N):
        import math
        x = math.log(N, 2)
        x = math.ceil(x)
        return int(x * 10)



t = Scissors()
print(t.openingTime(4))
print(t.openingTime(2))
print(t.openingTime(3))
print(t.openingTime(10))
print(t.openingTime(1000000000))