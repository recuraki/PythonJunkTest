"""
累積和
"""

class cumSum1D(object):
    sdat = []
    def init(self):
        pass
    def load(self, l):
        import itertools
        self.sdat = list(itertools.accumulate(itertools.chain([0], l)))
    def query(self, l, r):
        """
        query [l, r)
        """
        # assert l < r
        return self.sdat[r] - self.sdat[l]


cs = cumSum1D()
cs.load([1, 2, 3, 4, 5])
assert cs.query(0, 5) == 15
assert cs.query(1, 5) == 14
assert cs.query(2, 3) == 3
