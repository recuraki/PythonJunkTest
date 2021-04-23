import math

mw2dbm = lambda x: round(10 * math.log10(x), 3)
dbm2mw = lambda x: round(math.pow(10, x/10), 3)

class amp(object):
    def __init__(self):
        self.inminpower = -10 # dBm
        self.inmaxpower = +6 #dBm
        self.maxgain = 30 # dB
        self.output = 20 #dBm
        self.lasersdbm = []

        self.setup()

    def setup(self):
        self.outputmw = dbm2mw(self.output)

    def indbm(self, inlevel):
        if not (self.inminpower <= inlevel <= self.inmaxpower):
            raise
        self.lasersdbm.append(inlevel)
    def totalinmw(self):
        return round(sum([dbm2mw(x) for x in self.lasersdbm]), 3)
    def totalindbm(self):
        return round(mw2dbm(self.totalinmw()), 3)
    def amp(self, loss=0):
        assert self.totalinmw() < self.output
        lasersOutputdbm = self.lasersdbm
        lasersOutputmw = [round(dbm2mw(x),3) for x in self.lasersdbm]
        print("InLaser")
        print(" dBm", lasersOutputdbm)
        print(" mW", lasersOutputmw)
        print("InlaserTotal(dBm, mW) = {0} dBm, {1} mW".format(self.totalindbm(), self.totalinmw()))

        ampRatio = self.outputmw / self.totalinmw()
        lasersOutputmw = [round(dbm2mw(x) * ampRatio,3) for x in self.lasersdbm]
        lasersOutputdbm = [mw2dbm(x) for x in lasersOutputmw]
        print("Target: {0} mW => AmpRatio: {1}".format(self.outputmw, ampRatio))
        print("AmpedPower")
        print(" dBm", lasersOutputdbm)
        print(" mW", lasersOutputmw)
        lasersOutputdbm = [round(x - loss, 3) for x in lasersOutputdbm]
        lasersOutputmw = [round(dbm2mw(x), 3) for x in lasersOutputdbm]
        print("Dest: loss {0}dBm ".format(loss))
        print(" dBm", lasersOutputdbm)
        print(" mW", lasersOutputmw)


a = amp()
a.indbm(0)
a.indbm(-6)
a.indbm(-10)
print("inTotal")
print(" ", a.totalindbm(), "dBm")
print(" ", a.totalinmw(), "mW")
a.amp(28)